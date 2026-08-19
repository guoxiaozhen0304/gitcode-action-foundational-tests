用例 ID:   REL-FAULT-01-003
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-015
母意图:    —
标题:      模拟 runner 崩溃后 job 状态迁移与重调度

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发长时运行的 workflow
  2. 在执行中 kill runner 进程
  3. 验证 job 状态迁移
  4. 验证可重新触发 rerun

预期结果:
  1. job 状态变为 failure 或 cancelled
  2. 状态正确回写到 API
  3. rerun 可重新调度

验证点:
  - [正向] 状态为 failure
  - [正向] API 返回 failure 状态

清理:      fixture
