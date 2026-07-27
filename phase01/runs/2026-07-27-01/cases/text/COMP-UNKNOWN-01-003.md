用例 ID:   COMP-UNKNOWN-01-003
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-021
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/testorg/full_pr.yaml (2026-07-22)
母意图:    —
标题:      未声明 select 的 stage 与 job 默认被执行

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写不含任何 select 字段的 workflow（多 job）
  2. 手动触发，验证全部 job 默认执行

预期结果:
  - 未声明 select 的 stage/job 默认执行（与全部官方示例一致）

验证点:
  - [正向] 未声明 select 的 job 全部执行并输出标记
  - [负向] 不应出现未声明 select 的 job 被默认跳过

清理:      重置 fixture 仓库
