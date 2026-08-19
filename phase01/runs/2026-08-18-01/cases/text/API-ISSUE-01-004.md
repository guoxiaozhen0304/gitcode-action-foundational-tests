用例 ID:   API-ISSUE-01-004
维度标签:   ['completeness']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-ISSUE-002
母意图:    —
标题:      创建里程碑并关联到 Issue

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建里程碑
  2. 创建 Issue 并关联里程碑
  3. 验证里程碑统计

预期结果:
  1. 里程碑创建成功
  2. Issue 关联成功

验证点:
  - [正向] 里程碑创建成功
  - [正向] 里程碑标题正确

清理:      fixture
