用例 ID:   API-ISSUE-01-003
维度标签:   ['completeness', 'compatibility']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-ISSUE-002
母意图:    —
标题:      创建标签并关联到 Issue

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建标签
  2. 创建 Issue 并关联该标签
  3. 验证 Issue 详情包含标签

预期结果:
  1. 标签创建成功
  2. Issue 关联标签成功

验证点:
  - [正向] 标签创建成功
  - [正向] 标签名称正确

清理:      fixture
