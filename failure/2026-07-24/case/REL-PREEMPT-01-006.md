## 失败分诊 · REL-PREEMPT-01-006 · preemption events 越界值——配置 11 个应被拒绝

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 19a — `preemption.events` 仅允许 `[mr_id]`
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  concurrency:
    preemption:
      events: [push, pull_request, workflow_dispatch, schedule, tag, issue_comment, pull_request_comment, merge_requests, fork_pr, manual, pr]

  # 应改为（仅允许 mr_id）:
  concurrency:
    preemption:
      events: [mr_id]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 19a: "`preemption.events` 仅允许 `[mr_id]`。push 不是允许值。"

**置信度**: 高（平台 Schema 明确拒绝，11 个值中无一在允许列表中，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `events contains unsupported value` 错误
- **影响面**: 所有在 preemption.events 中使用非 mr_id 值的工作流
- **综合**: `preemption.events` 仅接受 `[mr_id]`，11 个事件值全部非法
- **是否有规避手段**: 是 — 改为 `events: [mr_id]`

**建议**:
- 将 `events` 列表替换为 `[mr_id]`；preemption events 多值测试需降级为单值 `mr_id`
