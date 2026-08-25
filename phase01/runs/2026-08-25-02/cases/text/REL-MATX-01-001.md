用例 ID:   REL-MATX-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-004
母意图:    —
标题:      matrix max-parallel=2 时矩阵展开实例并发度被限制

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发含 4 个矩阵实例且 max-parallel=2 的 workflow
  2. 通过 API 观察运行中 job 数量
  3. 验证并发度不超过 2

预期结果:
  1. 同时运行的 matrix 实例不超过 2 个
  2. 4 个实例全部完成

验证点:
  - [正向] 并发实例数不超过 2
  - [正向] 全部完成

清理:      none
