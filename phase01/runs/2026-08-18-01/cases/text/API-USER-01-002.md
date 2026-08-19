用例 ID:   API-USER-01-002
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-AUTH-001
母意图:    —
标题:      PAT 带正确 scope 可访问仓库 API

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['PAT_WITH_REPO_SCOPE']

操作步骤:
  1. 使用含 repo scope 的 PAT 调用仓库详情 API

预期结果:
  1. 认证成功，返回仓库详情

验证点:
  - [正向] PAT 认证成功
  - [正向] 返回仓库详情

清理:      none
