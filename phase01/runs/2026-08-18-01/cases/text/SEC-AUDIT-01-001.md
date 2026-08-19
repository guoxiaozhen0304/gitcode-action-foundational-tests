用例 ID:   SEC-AUDIT-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-019
母意图:    —
标题:      审计日志记录权限变更与 secret 访问事件

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 执行权限变更操作（如添加成员）
  2. 查询审计日志
  3. 验证日志包含该事件

预期结果:
  1. 审计日志包含权限变更记录
  2. 审计日志包含操作人、时间、操作类型

验证点:
  - [正向] 获取审计日志成功
  - [正向] 日志包含权限相关记录

清理:      none
