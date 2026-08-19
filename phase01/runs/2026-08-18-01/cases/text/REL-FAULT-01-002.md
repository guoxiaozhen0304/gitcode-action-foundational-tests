用例 ID:   REL-FAULT-01-002
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-014
母意图:    —
标题:      stress CPU 时 step 超时与心跳保活

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发 CPU 饱和测试 workflow
  2. 验证 job 在 timeout 前不会无响应
  3. 验证心跳保活机制有效

预期结果:
  1. job 要么在 10 分钟 timeout 时被终止，要么正常完成
  2. runner 不死锁
  3. 状态正确回写

验证点:
  - [正向] 超时后标记为 failure
  - [正向] 错误提及 timeout

清理:      fixture
