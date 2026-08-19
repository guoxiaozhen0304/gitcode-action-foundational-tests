用例 ID:   API-ISSUE-01-002
维度标签:   ['completeness']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-ISSUE-001
母意图:    —
标题:      创建 Issue 并关闭

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 通过 API 创建 Issue
  2. 验证返回状态为 open
  3. 通过 PATCH 关闭 Issue
  4. 验证状态变为 closed

预期结果:
  1. Issue 创建成功
  2. 关闭后状态为 closed

验证点:
  - [正向] Issue 创建成功
  - [正向] 初始状态为 open

清理:      fixture
