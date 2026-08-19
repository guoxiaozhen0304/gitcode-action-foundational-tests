用例 ID:   REL-STEPS-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-012
母意图:    —
标题:      单 job 16 个 step 的调度与状态回写完整性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发含 16 个 step 的 workflow
  2. 验证所有 step 按序执行
  3. 验证 API 返回的 steps 列表完整
  4. 验证每个 step 状态正确回写

预期结果:
  1. 16 个 step 全部执行
  2. API 返回的 steps 数量为 16
  3. 无 step 状态丢失

验证点:
  - [正向] workflow 完成
  - [正向] 最后一步执行

清理:      fixture
