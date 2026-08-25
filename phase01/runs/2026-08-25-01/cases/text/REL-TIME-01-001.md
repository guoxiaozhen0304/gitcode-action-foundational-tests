用例 ID:   REL-TIME-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-011
母意图:    —
标题:      job 运行 350 分钟观察正常终止 vs 超时 kill

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发运行 350 分钟的 job
  2. 在 350 分钟时检查状态
  3. 验证 job 正常完成而非被 kill
  4. 验证超时设置生效

预期结果:
  1. job 在 350 分钟左右正常完成
  2. 状态为 success
  3. 未被提前 kill

验证点:
  - [正向] 运行完成
  - [正向] 日志包含结束标记
  - [非功能] 耗时在 348-360 分钟之间

清理:      fixture
