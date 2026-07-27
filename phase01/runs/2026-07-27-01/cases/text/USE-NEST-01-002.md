用例 ID:   USE-NEST-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_call 嵌套 2 层时应正常执行

前置条件:
  - 仓库存在 2 层嵌套的 reusable workflow：
    - reusable-level1.yml（on: workflow_call，job 级调用 reusable-level2.yml）
    - reusable-level2.yml（on: workflow_call，含实际执行步骤，输出 level2 executed）

操作步骤:
  1. 主 workflow 以 job 级 uses 调用 reusable-level1.yml
  2. reusable-level1.yml 再以 job 级 uses 调用 reusable-level2.yml
  3. 触发主 workflow 并观察运行状态与日志

预期结果:
  运行成功完成，无嵌套层数报错；日志包含最内层步骤输出 level2 executed

验证点:
  - [正向] 运行成功完成（run 状态 COMPLETED）
  - [正向] 日志包含 level2 executed（嵌套链路真正执行到最内层）
  - [负向] 不应报嵌套超限错误

清理:      无
