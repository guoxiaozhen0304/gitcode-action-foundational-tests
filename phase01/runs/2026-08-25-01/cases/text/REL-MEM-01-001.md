用例 ID:   REL-MEM-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-023
母意图:    —
标题:      small runner 上申请 12GB 内存观察 OOM kill 行为

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 在 small runner 上申请 12GB 内存
  2. 验证进程被 OOM kill
  3. 验证 job 状态正确标记为 failure
  4. 验证 runner 未崩溃

预期结果:
  1. 进程被 kill
  2. job 状态为 failure
  3. 错误信息包含 OOM 或 killed

验证点:
  - [正向] job 失败
  - [正向] 报错清晰

清理:      fixture
