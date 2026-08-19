用例 ID:   SEC-ROLE-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-013
母意图:    —
标题:      Developer 角色不得修改仓库设置或管理 secrets

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以 Developer 身份调用修改仓库设置 API
  2. 验证返回 403

预期结果:
  1. Developer 无权限修改设置
  2. 返回 403

验证点:
  - [负向] 修改设置被拒绝

清理:      none
