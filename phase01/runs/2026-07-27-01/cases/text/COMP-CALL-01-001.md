用例 ID:   COMP-CALL-01-001
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-006
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      2 层 workflow_call 嵌套正常执行

前置条件:
  - fixture 仓库 reusable-workflow 提供可复用子 workflow（.gitcode/workflows/reusable-sub.yml，on 为 workflow_call，其步骤输出固定 marker 字符串 sub_workflow_marker）
  - 主 workflow 的 caller job 通过 job 级 uses 调用该子 workflow（主 -> 子共 2 层）

操作步骤:
  1. 手动触发主 workflow
  2. caller job 通过 job 级 uses 调用子 workflow
  3. 观察嵌套调用是否成功完成，并检查运行日志中是否出现子 workflow 步骤的 marker

预期结果:
  - 2 层嵌套 workflow_call 成功执行，运行状态成功
  - 子 workflow 的步骤日志（marker）出现在本次运行的日志中

验证点:
  - [正向] 运行状态成功
  - [正向] 子 workflow 的 step 日志 marker 可见

清理:      none
