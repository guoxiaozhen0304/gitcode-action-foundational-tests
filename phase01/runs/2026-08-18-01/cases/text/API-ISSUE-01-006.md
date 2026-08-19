用例 ID:   API-ISSUE-01-006
维度标签:   ['completeness']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-ISSUE-004
母意图:    —
标题:      MR 描述含 close 关键字合并后自动关闭 Issue

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建 MR 描述含 close #issue_number
  2. 合并 MR
  3. 验证 Issue 状态自动变为 closed

预期结果:
  1. MR 合并成功
  2. 关联 Issue 自动关闭

验证点:
  - [正向] MR 创建成功

清理:      fixture
