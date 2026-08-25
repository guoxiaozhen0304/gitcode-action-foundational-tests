用例 ID:   SEC-ROLE-01-002
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-013
母意图:    —
标题:      Reporter 角色不得触发 workflow_dispatch

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以 Reporter 身份调用 workflow_dispatch API
  2. 验证返回 403

预期结果:
  1. Reporter 无权限触发 workflow
  2. 返回 403 或 404

验证点:
  - [负向] 触发 workflow 被拒绝

清理:      none
