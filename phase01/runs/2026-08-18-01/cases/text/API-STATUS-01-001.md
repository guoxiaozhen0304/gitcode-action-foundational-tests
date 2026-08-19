用例 ID:   API-STATUS-01-001
维度标签:   ['completeness']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-HOOK-002
母意图:    —
标题:      创建 Commit Status 并关联到 MR

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 对指定 commit SHA 创建 success 状态
  2. 验证 MR 详情页显示该状态
  3. 验证状态列表包含 context

预期结果:
  1. 状态创建成功
  2. MR 关联显示 CI 通过

验证点:
  - [正向] 状态创建成功
  - [正向] 状态为 success

清理:      fixture
