用例 ID:   API-BRANCH-01-004
维度标签:   ['completeness', 'compatibility']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-GIT-004
母意图:    —
标题:      通过 API 创建分支

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 基于 main 创建新分支

预期结果:
  1. 分支创建成功，返回 201

验证点:
  - [正向] 分支创建成功
  - [正向] 返回分支名称正确

清理:      fixture
