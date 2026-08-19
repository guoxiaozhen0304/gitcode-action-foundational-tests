用例 ID:   API-USER-01-003
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-AUTH-001
母意图:    —
标题:      PAT 无 repo scope 时访问仓库 API 返回 403

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['PAT_NO_REPO_SCOPE']

操作步骤:
  1. 使用不含 repo scope 的 PAT 调用仓库详情 API

预期结果:
  1. 认证通过但权限不足，返回 403 或 401

验证点:
  - [负向] 无 scope 时拒绝访问

清理:      none
