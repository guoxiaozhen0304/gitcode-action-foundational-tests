用例 ID:   API-USER-01-005
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-AUTH-002
母意图:    —
标题:      Reporter 角色不可推送代码

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以 Reporter 身份尝试推送代码到仓库

预期结果:
  1. 推送被拒绝，返回非 0 退出码

验证点:
  - [负向] Reporter 推送被拒绝
  - [正向] 错误信息包含权限拒绝

清理:      none
