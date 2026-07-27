# Classify-Experiment Agent / 案例可脚本化分类 Agent

## 角色定位
你是 Phase 02 的**案例分类辅助**。对每个 case YAML 做 trigger + setup + fault_injection + 断言的全链路可脚本化分析，判断能否被 `workflow_runner.py` + `assertion_engine.py` 全自动执行。

## 分类步骤

### Step 1: 校验（validate）

对一批 case YAML 逐条提交到平台 API 校验，按结果分组：

```bash
cd phase02/classify-experiment/2026-07-23
python3 batch_validate.py
# 输入: phase01/runs/<run-id>/cases/yaml/
# 输出:
#   VALID/          ← 平台校验通过
#   INVALID/        ← 平台校验驳回
#   SKIP/           ← 无 workflow 字段
#   validation-results.json
```

**WAF 拦截处理**: 若 API 返回 HTTP 418 (WAF 拦截)，检查 `quick-start.md` 中的 WAF 白名单。若该 case 在 quick-start 中标注为 "人工验证通过"，则同样移至 `VALID/`。其他 WAF 拦截 case 暂存留待人工判断。

### Step 2: 可脚本化分类（classify）

只对 `VALID/` 中的 case 做分类。逐 case 检查三个维度：

#### 2a. Trigger 层 — 能否用 API 触发 workflow？

| 触发事件 | API 调用链 | 平台是否触发 | 分类标签 |
|----------|-----------|-------------|---------|
| `push` | `git push` | ✅ 已验证 | `scriptable` |
| `pull_request` | `POST /pulls` | ✅ 已验证 | `scriptable` |
| `pull_request_target` | `POST /pulls` (fork) | ✅ 已验证 | `scriptable` |
| `fork_pr` | `POST /forks` + `POST /pulls` | ✅ 已验证 | `scriptable` |
| `issue_comment` | `POST /issues` + `POST /comments` | ✅ 已验证 | `scriptable` |
| `pull_request_comment` | `POST /comments` (PR) | ✅ 已验证 | `scriptable` |
| `schedule` | push cron + wait | ⚠️ 变通可行但不稳定 | `api_blocked` |
| `workflow_dispatch` / `manual` | ✅ 已验证 | `scriptable` |
| `tag` | `git tag` + push | ❓ 未验证 | `untested` |

**原则**: 
- trigger ∈ {push} → 继续检查 setup + 断言
- trigger ∈ {pull_request, issue_comment, schedule, ...} → `api_blocked`（API 已证明可行，但平台不触发 — 非代码问题）
- trigger ∈ {workflow_dispatch, tag, manual} → `untested`（dispatch API 尚未批量验证）

#### 2b. Setup/Fault 层 — 环境是否就绪？

- `repo_fixture` 不在已知 fixture 列表中 → `fixture_gap`
- `fault_injection` 有 action 但平台不支持（如 `kill_runner`, `network_partition` 不生效）→ `fault_gap`

**已知 fixture**:
```
basic-ci, clean, default, with-secrets, fork-target, fork-source,
environment-protected, private-registry, large-repo, runner-release, badge-test
```

#### 2c. 断言层 — 断言引擎能否执行？

检查每个 `assertions[]` 项的 `target` 字段：

| target | 对应 kind | 引擎状态 | 说明 |
|--------|----------|---------|------|
| `run_status` | `run_status` | ✅ 已实现 | conclusion 字符串比对 |
| `run_logs` | `status` / `value` / `leak` | ✅ 已实现 | 日志扫描 |
| `run_logs` + `must_not_contain_secret` | `leak` | ✅ 已实现 | 明文 secret 检测 |
| `step_summary` | `value` | ⚠️ `assertion_gap` | 需从 run 对象读取 step_summary 字段 |
| `artifacts` | `artifact_download` | ⚠️ `assertion_gap` | 需下载 artifact 后检查内容 |
| `cache_contents` | `cache_pollution` | ⚠️ `assertion_gap` | 需触发 cache restore 后扫描 |
| `run_ui` / `pr_ui` | `pr_ui` | ⚠️ `assertion_gap` | 需 Playwright 截图 + LLM |
| `eval=llm_assisted` | `llm` | ⚠️ `assertion_gap` | 需 LLM 集成 |

**判定规则**:
- 全部 target 的 kind 都在 ENGINE_KINDS 中 → 断言层 OK
- 任一 target 需要新 assertion kind 且全部 mappable=0 → `assertion_gap`
- 仅有 `llm` target → `assertion_gap`（需要 LLM 集成）

**ENGINE_KINDS**（已实现）: `run_status`, `status`, `value`, `leak`, `mask`, `config_probe`

### Step 3: 输出

```bash
python3 classify_20260723.py
# 输出: classification_report.md
```

报告结构：
```
## 总体统计 (各类别数量 + 占比)
## 按维度 × 分类 (交叉表)
## 阻断项汇总 (按 trigger/setup/fault/assertion 分组)
## 逐 Case 明细 (每个 case 的分类 + 阻断原因 + 断言详情)
```

### Step 4: 无效案例分诊

对 INVALID 和 ERROR 案例生成故障分析报告，区分：
- **预期非法** (negative test): case 有意测试平台报错能力，INVALID 是期望结果
- **非预期非法**: case 描述正常功能但被平台校验驳回，属于平台缺陷或 case bug

分析原则遵循 `phase02/agents/failure-analyst/CLAUDE.md`。

### Step 5: 快速上手文档

更新 `phase02/classify-experiment/quick-start.md`，包含完整工作流和最新批次结果。

---

## 分类标签总结

| 标签 | 含义 | 优先级 |
|------|------|--------|
| `scriptable` | trigger 可触发 + 全部断言可映射 + 环境就绪 | 0 |
| `assertion_gap` | trigger 可触发，但断言需新 kind | 1 |
| `fixture_gap` | trigger 可触发，但缺 repo fixture | 2 |
| `fault_gap` | 需要故障注入基础设施 | 3 |
| `untested` | trigger API 尚未验证 | 4 |
| `api_blocked` | API 调用可行，平台不触发 workflow | 5 |

---

## 断言 Gap 分析示例: `artifacts` target

**案例**: `SEC-SIDECHAN-02-001` — "Secret 不经 output / artifact / step summary 侧信道绕过脱敏外泄"

```yaml
assertions:
  - type: negative
    target: run_logs
    must_not_contain_secret: "SIDECHAN_SECRET"
  - type: negative
    target: step_summary
    eval: "deterministic"
    rubric: "step summary 不含 secret 明文"
  - type: negative
    target: artifacts    # ← 需要 artifact_download
    eval: "deterministic"
    rubric: "artifact 内容不含 secret 明文"
```

**分析**:

1. `target: run_logs` → kind=`leak` → ✅ 已实现（日志扫描明文 secret）
2. `target: step_summary` → kind=`value` ⚠️ 需从 workflow run 对象读取 `step_summary` 字段值并检查是否含 secret — `assertion_gap`, API 已确认 (`GET /api/v8/.../runs/:id/jobs/:jid/download_log`)
3. `target: artifacts` → kind=`artifact_download` ⚠️ 需:
   - 通过 API 下载 artifact (`GET /api/v8/.../artifacts/:id/download`)
   - 检查 artifact 内容是否包含明文 secret "SIDECHAN_SECRET"
   - 已通过 demo 验证下载链路可行 (`demo_artifact_assertion.py`)，待写入 assertion_engine

**分类结果**: `assertion_gap` (push trigger 可用，但 `step_summary` + `artifacts` 两个 target 需新 assertion kind)

**数据流**:
```
upload-artifact → platform store → GET /api/v8/.../artifacts/:id/download
                                                    ↓
                                          extract & grep secret = SIDECHAN_SECRET
                                                    ↓
                                          must_not_contain → PASS/FAIL
```
