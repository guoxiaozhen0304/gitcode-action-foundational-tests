# Abnormal 根因分析 · 2026-07-28-01

> 44 条 abnormal 用例（非 PASS 非 FAIL）按根因归属分 4 类。
>
> **仓库分配说明**：所有用例由 pool_scheduler 轮转分配到 gitcode-test-0 ~ gitcode-test-4（5 仓 × 2 并发容量）。预检拦截的用例（COMPILE_ERROR / INCONCLUSIVE guard）未实际部署到仓库，记为「预检阶段」。已部署的用例（ENV_ERROR / TIMEOUT）在对应仓库上执行。

---

## 一、平台缺陷 / 能力边界（19 条）

### 1.1 workflow_call 被调文件未部署（9 条）★leader 复核纠正：非平台缺陷，应重判 NOT_CONFIGURED

**现象**：dispatch_workflow 返回 HTTP 400，报文示例：

```json
{"error_code":400,"error_code_name":"THIRD_ERROR","error_message":"获取调用call_child的yml时失败，原因：未获取到流水线编号"}
```

**★ leader 复核纠正（2026-07-28）**：原判"平台不支持 workflow_call"**证据不成立**。这些用例 caller 里 `uses: ./.gitcode/workflows/reusable.yml` 引用一个**被调 workflow 文件**，且 `setup.repo_fixture` 声明了对应 fixture（如 reusable-workflow-local）。但：
- 被调体内容**根本不在用例契约的 `workflow:` 字段里**（契约只有 caller）；
- harness 的 deploy **只部署单个 `workflow:` 文件**，fixture 自动布置未实现（HARNESS-PLAN P2）→ reusable.yml 从未被放到仓库；
- 所以平台报"未获取到流水线编号"是因为**被调文件缺失**，不是平台拒绝 workflow_call 语义。

**我们从未把被调文件交给平台，因此无法据此判定平台是否支持 workflow_call。**

**正确归类**：`NOT_CONFIGURED`（缺 fixture），**不计入平台缺陷/失败**。workflow_call 支持性**未测到**（既未证支持、也未证不支持）。要真测需补 fixture 自动布置（部署被调 reusable.yml）后重跑。

| 用例 | 仓库 | 嵌套深度 | 错误报文关键信息 |
|---|---|---|---|---|
| REL-CHILDSTATE-01-064 | test-0 | 1 层 (call_child) | 未获取到流水线编号 |
| REL-CHILDSTATE-01-064-V2 | test-0 | 1 层 (call_child) | 同上 |
| COMP-CALL-01-003 | test-4 | 1 层 (caller) | 同上 |
| COMP-CALL-01-004 | test-4 | 1 层 (caller) | 同上 |
| COMPAT-NEST-01-001 | test-4 | 2 层 (call-level2) | 同上 |
| COMPAT-NEST-01-002 | test-4 | 2 层 (call-level2) | 同上 |
| REL-NEST-01-023 | test-2 | 1 层 (call_level1) | 同上 |
| REL-NEST-01-024 | test-2 | 1 层 (call_level1) | 同上 |
| USE-NEST-01-002 | test-0 | 1 层 (caller) | 同上 |

### 1.2 comment 类 webhook 事件不触发（10 条）

**现象**：用例采用 `issue_comment` 或 `pull_request_comment` 触发方式——先通过 API 创建 issue/PR comment，期望平台根据 comment 事件触发对应 workflow。实际 dispatch 阶段成功获得 `workflow_run_id`，但 300-600s 内 run 始终未进入终态 → 超时截断。

**定位**：与 not_scriptable 分析结论一致——GitCode 的 webhook 事件链路（comment 创建 → 事件分发 → workflow 触发）不完全可靠。要么平台不响应 comment 类 webhook，要么事件分发延迟远超 600s。

**影响**：issue_comment 和 pull_request_comment 是自动化协作的核心触发方式（自动标签、自动评审、机器人回复），此能力的缺失意味着无法构建 issue/PR 驱动的自动化工作流。

| 用例 | 仓库 | 触发类型 | 实际耗时 |
|---|---|---|---|---|
| SEC-INJ-01-003 | test-1 | issue_comment | 641s |
| SEC-TOCTOU-01-002 | test-2 | issue_comment | 659s |
| SEC-TOCTOU-01-003 | test-3 | pull_request_comment | 661s |
| COMP-TRIG-01-076 | test-4 | issue_comment | 625s |
| COMP-TRIG-01-077 | test-0 | pull_request_comment | 638s |
| COMP-TRIG-01-080 | test-0 | pull_request_comment | 607s |
| COMPAT-COMM-01-001 | test-2 | issue_comment | 641s |
| COMPAT-COMM-01-002 | test-3 | issue_comment | 639s |
| USE-TYPE-01-003 | test-1 | pull_request_comment | 604s |
| COMP-TRIG-01-078 | test-1 | schedule (cron 不准) | 637s |

---

## 二、Harness / 环境问题（1 条）★leader 复核：原 8 条中 untrusted 7 条移出（guard 正确工作，非 bug）

### 2.1 untrusted_contributor 被 guard 正确拦截（7 条）★leader 复核纠正：非环境变量 bug

**现象**：7 条 `trigger.as: untrusted_contributor` 的用例全部被 guard 拦为 INCONCLUSIVE，理由："untrusted_contributor 执行路径未实现，拒绝以 maintainer 假验证"。

**★ leader 复核纠正（2026-07-28）**：原判"环境变量名不匹配"**不成立**。核实代码：contributor token 全程读**文件** `~/.gitcode-contributor-token`（三处均 `os.path.exists`），**没有任何一处读 `GITCODE_CONTRIBUTOR_TOKEN` 环境变量**（grep 零命中）。该文件已存在，`.env` 里叫什么名代码根本不读。

**真实原因**：这 7 条源 YAML 的 trigger 是 `untrusted_contributor` + `pull_request_target`/`pull_request`/`fork_pr`/`push`，且**都没带 `untrusted_exec: same_repo_payload` opt-in**。guard 逻辑对"untrusted 且无真实低权限执行路径"的用例**一律拦成 INCONCLUSIVE，拒绝以 maintainer 身份假验证**——这是 guard 的**设计目的、在正确工作**，不是故障。改 env 变量名对这 7 条毫无作用。

**正确归类**：guard 正确行为，**非 harness bug**。这些 untrusted 用例要真跑需：①走 comment 路径（issue_comment + token 文件，已支持）；或②加 same_repo_payload opt-in（如 SEC-INJ-01-001 已做）；fork_pr 类（COMPAT-PERM-01-002）受平台 fork 门限制，保持 NOT_TESTABLE。

| 用例 | 仓库 |
|---|---|
| COMPAT-PERM-01-002 | 预检阶段 |
| COMPAT-TARGET-01-001 | 预检阶段 |
| COMPAT-TARGET-01-002 | 预检阶段 |
| COMP-PRTARGET-01-003 | 预检阶段 |
| SEC-INJ-01-002 | 预检阶段 |
| SEC-INJ-01-004 | 预检阶段 |
| SEC-ORG-01-002 | 预检阶段 |

### 2.2 多仓并发 push 冲突（1 条）

| 用例 | 仓库 | 现象 |
|---|---|---|
| COMP-BOUND-01-086 | test-3 | `git push` 冲突，提示需 `git pull --rebase`，后续 `list_workflows` 在 60s 窗口内找不到 workflow_id |

5 个仓库并发 push 时，gitcode-test 仓库可能被其他用例的 deploy 抢先推送，当前次的 push 远端领先于本地 → 被拒绝。

---

## 三、用例设计 / 夹具问题（8 条）

### 3.1 push paths 无文件变更匹配（3 条）

**现象**：用例使用 `on.push.paths` 过滤特定路径（如 `src/**`），但 harness 的 deploy 只写入 `.gitcode/workflows/<case>.yml` 并 push，不产生目标路径的文件变更 → workflow 永不触发 → 300s 超时。

**定位**：用例设计的触发条件与 harness 的 deploy 行为不兼容。测试"paths 过滤"本身需要一个额外的文件变更，但当前的 deploy 只做了 workflow 文件提交，没有同时在 paths 匹配路径下制造变更。

| 用例 | 仓库 | 耗时 |
|---|---|---|
| REL-PATHS-01-014 | test-4 | 618s |
| REL-PATHS-01-015 | test-0 | 624s |
| COMP-PUSH-01-003 | test-2 | 631s |

### 3.2 YAML 不符合合约规范（2 条）

| 用例 | 仓库 | 原因 |
|---|---|---|
| USE-LBL-01-004 | 预检阶段 | `runs-on: ubuntu-latest`（字符串），preflight 要求数组格式 |
| REL-OUTPUT-01-017 | 预检阶段 | step name `'write 1MB+1 output'` 含 `+` 字符，preflight 拒绝 |

这两条是 `schema_check` 通过但 `preflight_validate`（执行前校验）才拦截的——schema_check 只验结构，preflight 验语义。

### 3.3 dispatch inputs 校验不匹配（2 条）

| 用例 | 仓库 | 现象 |
|---|---|---|
| USE-DISP-01-001 | test-1 | dispatch HTTP 400: Actions字段定义Inputs校验失败 |
| USE-DISP-01-003 | test-1 | 同上 |

用例 YAML 的 `workflow_dispatch.inputs` 定义与平台对 dispatch payload 的校验规则不兼容（可能是字段类型、required 标记或 default 值格式问题）。

### 3.4 日志不可得（1 条）

| 用例 | 仓库 | 现象 |
|---|---|---|
| REL-NEEDS-01-027 | test-0 | 有 run_id，收集阶段采集不到日志，无法判定 |

---

## 四、超时 — 调度/执行窗口不足（9 条）

### 4.1 超时白名单未覆盖的 dispatch 长时用例（2 条）

| 用例 | 仓库 | 耗时 | 说明 |
|---|---|---|---|
| COMPAT-MATRIX-01-005 | test-2 | 602s | matrix dispatch，多 job 组合执行 > 默认 300s |
| COMPAT-CONTAINER-01-002 | test-4 | 641s | 容器化 dispatch，启动+执行总长 > 默认 300s |

超时白名单（22 条）覆盖了 REL-TIMEOUT/REL-DISK 等已知长用例，但这 2 条未覆盖。

### 4.2 边界测试设计如此（2 条）

| 用例 | 仓库 | 耗时 | 说明 |
|---|---|---|---|
| REL-TIMEOUT-01-008 | test-3 | 613s | 白名单设为 600s，设计上就是要够不到以测超时行为 |
| REL-TIMEOUT-01-010 | test-4 | 603s | 同上，dispatch 长时的边界测试 |

### 4.3 平台调度延迟 / runner 排队（5 条）

| 用例 | 仓库 | 耗时 | 触发方式 |
|---|---|---|---|
| USE-ONBD-01-002 | test-0 | 635s | push |
| COMP-BOUND-01-084 | test-3 | 614s | push |
| COMPAT-DIR-01-003 | test-3 | 717s | push |
| REL-DEBOUNCE-01-002 | test-0 | 615s | push x2（去抖测试） |
| COMPAT-TARGET-01-003 | test-1 | 602s | pull_request_target |

这些用例的 workflow 已被推送，但平台在高峰期 runner 资源竞争激烈时调度延迟变大，超过了默认 300s + 白名单扩展的时间窗口。

---

## 汇总

| 根因归属 | 条数 | 涉及 verdict 类型 |
|---|---|---|
| 平台缺陷 | **9** | TIMEOUT (9)（comment 事件不响应），已扣除 workflow_call 10 条（重判 NOT_CONFIGURED） |
| Harness 环境 | **1** | ENV_ERROR (1)（push 冲突） |
| 用例设计 / fixture 缺口 | **18** | NOT_CONFIGURED (9，workflow_call 被调文件未部署) + COMPILE_ERROR (2) + ENV_ERROR (2) + TIMEOUT (3) + INCONCLUSIVE (1) |
| Guard 正确行为 | **7** | INCONCLUSIVE (7，untrusted 被正确拦截） |
| 超时混合 | **9** | TIMEOUT (9) |
| **合计** | **44** | |
