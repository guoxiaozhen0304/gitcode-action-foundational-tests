用例 ID:   REL-MATX-01-003
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-008
母意图:    —
标题:      矩阵组合数超过平台上限时应报错或拒绝

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 提交矩阵组合数极大的 workflow（32 组合）
  2. 验证平台是否拒绝或正确调度

预期结果:
  1. 平台正确展开所有组合，或给出清晰的超限报错

验证点:
  - [正向] 超限时报错清晰
  - [正向] 若接受则全部完成

清理:      fixture
