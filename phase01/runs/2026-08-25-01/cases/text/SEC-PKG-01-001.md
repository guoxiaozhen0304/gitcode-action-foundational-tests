用例 ID:   SEC-PKG-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-017
母意图:    —
标题:      低权限用户不得覆盖或删除已有包版本

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以 Developer 身份尝试删除已发布的包版本
  2. 验证返回 403

预期结果:
  1. 删除操作被拒绝
  2. 返回 403

验证点:
  - [负向] 删除包版本被拒绝

清理:      none
