用例 ID:   REL-CONC-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-002
母意图:    —
标题:      短时间内高频触发同仓库 workflow 的排队与公平性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 快速连续触发 10 次 workflow_dispatch
  2. 通过 API 查询运行中 runs 数量
  3. 验证排队行为与公平性

预期结果:
  1. 同时运行数不超过 max=3
  2. 超出部分进入 QUEUE 状态
  3. 无 run 被静默丢弃

验证点:
  - [正向] 并发运行数不超过 3
  - [非功能] 排队等待时间不超过 3 分钟

清理:      none
