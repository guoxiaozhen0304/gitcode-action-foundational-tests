用例 ID:   API-ISSUE-01-005
维度标签:   ['completeness', 'usability']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-ISSUE-003
母意图:    —
标题:      创建 Issue 评论并包含 @提及

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 在 Issue 下创建含 @提及的评论

预期结果:
  1. 评论创建成功
  2. 内容完整保留 @提及

验证点:
  - [正向] 评论创建成功
  - [正向] 评论内容含 @提及

清理:      fixture
