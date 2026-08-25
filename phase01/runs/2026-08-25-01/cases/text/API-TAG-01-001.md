用例 ID:   API-TAG-01-001
维度标签:   ['completeness']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-GIT-004
母意图:    —
标题:      通过 API 创建 Release 与 Tag

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 创建 Release

预期结果:
  1. Release 创建成功
  2. Tag 同步创建

验证点:
  - [正向] Release 创建成功
  - [正向] Tag 名称正确

清理:      fixture
