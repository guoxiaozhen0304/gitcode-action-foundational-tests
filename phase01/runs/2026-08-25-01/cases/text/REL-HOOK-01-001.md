用例 ID:   REL-HOOK-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-019
母意图:    —
标题:      Webhook 接收端 5xx 时观察重试间隔与风暴抑制

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 配置指向 5xx 模拟端的 Webhook
  2. 触发测试投递
  3. 观察重试次数与间隔
  4. 验证无风暴式请求

预期结果:
  1. 重试次数有限（如 3-5 次）
  2. 重试间隔递增
  3. 总请求数可控

验证点:
  - [正向] 模拟端收到请求
  - [非功能] 重试次数不超过 5 次

清理:      fixture
