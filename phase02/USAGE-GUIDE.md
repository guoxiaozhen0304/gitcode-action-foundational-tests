# Phase 02 Harness · 完整使用指南

> 面向新用户：从零把一批 Phase 01 可执行 YAML 用例，在真实 GitCode 平台上跑出一份可信的分维度测试报告。
> 覆盖：全流程命令、两种执行模式、配置、判定模型、harness 内 4 个 LLM agent 的职责、当前触发器支持、**近期实测坑点**。
> ★ 判定铁律：pass/fail 只由确定性脚本（assertion_engine）裁决，LLM agent 只做只读辅助，不参与判定。

---

## 0. 全流程一图

```
Phase01 可执行 YAML（classify-experiment/<日期>/VALID 等）
   │
   ├─①─ schema_check.py ──→ queue.json（通过）/ rejected.json（拒收，回流 Phase01）
   │
   ├─②─ compile_asserts.py ──→ compiled/<cid>.asserts.json（rubric→value/leak/mask/run_status…）
   │
   ├─③─ pool_scheduler.py（并发）/ run_batch.py（顺序）
   │        deploy(git push) → 触发 → 精确匹配 run → 采集日志 → assertion_engine 判定 → 落库
   │
   └─④─ report_builder.py ──→ 分维度通过率 + 门禁结论 + 回归 diff
```

主链路全是确定性 Python。LLM agent（failure-analyst 等）只在旁路做只读辅助。

---

## 1. 前置条件

| 项 | 说明 | 位置 |
|---|---|---|
| GitCode OAuth token | git push + v8 API（日志采集） | `~/.gitcode-token` 或环境变量 `GITCODE_ACCESS_TOKEN` |
| GITCODE_COOKIE | **dispatch 触发专用**（web-api v2，JWT） | 工程根 `.env` 的 `GITCODE_COOKIE=`（脚本向上遍历 4 级目录找） |
| contributor token | fork/untrusted 场景（第二账号） | `~/.gitcode-contributor-token`（★不回显） |
| 测试仓池 | 可随意破坏的独立仓 | `ComputingActionTest/gitcode-test-0..4`（见 pool-config.yaml） |
| Python | 仅依赖 PyYAML | — |
| Phase01 产物 | 可执行 YAML | `phase02/classify-experiment/<日期>/VALID/` 等 |

★ **cookie 有效期短**，长时全量跑中途会过期 → 见坑点 §7.1。开跑前务必预检。

---

## 2. 并发全流程（推荐，多仓池）

```bash
cd D:/user/code/gitcode-action-foundational-tests

# ① schema 校验（--src-dir 指向任意用例目录）
python phase02/scripts/schema_check.py <p1-id> <run-id> --src-dir phase02/classify-experiment/2026-07-23/VALID

# ② 断言编译（rubric → 引擎可判的断言）
python phase02/scripts/compile_asserts.py <p1-id> <run-id> --src-dir phase02/classify-experiment/2026-07-23/VALID

# ★③ 开跑前预检 cookie（省 60 条 ENV_ERROR 的教训，见 §7.1）
python phase02/scripts/run_case.py phase02/classify-experiment/2026-07-23/VALID/COMP-ARTIFACT-01-001.yaml <run-id>-precheck
#   —— 这条无 atomgit/inputs/workflow_call，dispatch 应返 200；若 401/400 停下排查

# ④ 并发执行（多仓池）
python phase02/scripts/pool_scheduler.py <run-id> [--only c1,c2] [--no-logs]

# ⑤ 报告（--compare 出回归 diff）
python phase02/scripts/report_builder.py <run-id> --compare <上一个-run-id>

# 中途查看实时进度（只读）
python phase02/scripts/status.py <run-id>
```

**★ run-id 每次必须全新，不复用**（复用会让 summary.json 多轮累加污染，见 §7.3）。

---

## 3. 顺序全流程（CI 友好，无并发）

把上面的 ③ 换成：
```bash
python phase02/scripts/run_batch.py <run-id> [--no-logs] [--only c1,c2]
```
功能与 pool_scheduler 一致、逐条串行，慢但稳，适合 CI。

## 4. 单条调试

```bash
python phase02/scripts/run_case.py <contract.yaml> <run-id> [--no-logs]
```

---

## 5. 配置：pool-config.yaml

```yaml
repo_pool:
  owner: ComputingActionTest
  naming: "gitcode-test-{n}"   # 生成 gitcode-test-0 .. gitcode-test-4
  count: 5
  branch: main
queue:
  per_repo_capacity: 2          # 每仓最多 2 条在途 → 最大并发 10
polling:
  interval_seconds: 8
  case_timeout_seconds: 300     # ★全局超时；长时用例靠白名单覆盖（见 §7.6）
execution:
  teardown: batch_end           # 整批结束一次性清理
```

---

## 6. 判定模型（内部 verdict → 对外三态）

| 内部 verdict | 对外结论 | 计入通过率分母？ |
|---|---|---|
| PASS | 通过 | ✅ |
| FAIL（平台缺陷） | 问题发现 | ✅ |
| FAIL（用例/断言自身问题） | 回流 Phase01 修，不甩锅平台 | ✅ |
| INCONCLUSIVE | 未发现问题 | ❌ 剔除 |
| NOT_CONFIGURED / NO_RUN / ENV_ERROR / TIMEOUT / COMPILE_ERROR | 不可测试 | ❌ 剔除 |

- **假绿守卫**：run=COMPLETED 但无 job/step 或日志为空 → 一律不判 PASS。
- **通过率** = PASS /（PASS + FAIL），剔除"不可测试/未发现问题"。
- 归因（FAIL 是平台缺陷还是用例问题）由 failure-analyst 初判，**事实来源是 GitCode 官方文档**，agent 只给信号不改判定。

### run 目录结构（`phase02/runs/<run-id>/`）
`run.md`（元信息）· `queue.json`（执行队列）· `rejected.json`（拒收）· `state.json`（★实时计数，仅最后一轮）· `summary.json`（★全量累加，按 case_id）· `results/<id>.json`+`.log.txt`（每条证据）。

---

## 7. harness 内 4 个 LLM Agent（只读辅助，不碰判定）

> 定义在 `phase02/agents/<name>/CLAUDE.md`。全部只读、只给信号，pass/fail 仍归 assertion_engine。

| Agent | 角色 | 输入 | 产出 | 边界 |
|---|---|---|---|---|
| **harness-orchestrator** | 执行总指挥（Pipeline Controller）：排队列、控并发、异常升级（重试/跳过/中止）、状态机、`full_instance` 独占窗口 | INPUTS.md、queue、rules/process | 执行编排决策 | 不亲自跑用例/调 API/判定 |
| **failure-analyst** | 失败根因初判：FAIL 后分诊为「产品缺陷/用例问题/环境问题/需人工判断」 | Job 日志 + 用例 assertions + intent | 分类 + 证据（加速人工分诊的信号） | **不改判定结果**；事实来源=GitCode 官方文档，非 GitHub |
| **yaml-checker** | workflow 合规检查：拿 Phase01 交付的 YAML 对照 GitCode 文档查合规、能否被平台解析 | 用例 YAML + gitcode-spec | 合规/不合规+具体问题，回流 Phase01 | **不编写/改写/编译 YAML**（编写归 Phase01）；机器可判部分已由 preflight 覆盖，本 agent 未完全接线 |
| **expect-execute-consistency** | 假测试识别：workflow steps 是否真产生 assertions 期望的可观测输出（防 `echo "期望串"` 式空洞断言） | 用例 YAML（steps + assertions） | VACUOUS/真实 判定 | 判"步骤是否真执行被测功能"，非 harness 能否验证 |

---

## 8. 当前触发器支持现状

| 触发 | 状态 | 说明 |
|---|---|---|
| push | ✅ 硬证 | 主力，稳定 |
| workflow_dispatch / manual | ✅ 已验 | 需 cookie JWT |
| tag | 🟡 平台侧有证 | event=CreateTag |
| pr / pull_request（同仓） | ✅ 已验 | event=MR，47 条实测 |
| pull_request_target | 🟡 平台侧有证 | 端到端待坐实 |
| issue_comment / pull_request_comment | 🔧 已改建 Issue+评 Issue 路径 + contributor token | event 名待坐实 |
| schedule | ✅ 已跑通 | 6 位 Quartz cron；pool 注入 `0 * * * * ?` |
| **fork_pr** | ⛔ supported=False | 平台不自动触发 fork PR 的 on:pull_request（安全门，需批准），相关安全用例判 NOT_TESTABLE |

<!-- APPEND-3 -->

