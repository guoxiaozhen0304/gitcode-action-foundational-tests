用例 ID:   API-USER-01-004
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-AUTH-002
母意图:    —
标题:      Developer 角色不可修改保护分支规则

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以 Developer 身份调用设置保护分支 API

预期结果:
  1. Developer 角色无权限修改保护分支，返回 403

验证点:
  - [负向] Developer 无权修改保护规则

清理:      none
