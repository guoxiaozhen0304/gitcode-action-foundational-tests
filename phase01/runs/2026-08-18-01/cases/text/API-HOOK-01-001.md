用例 ID:   API-HOOK-01-001
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-HOOK-001
母意图:    —
标题:      创建 Webhook 并验证事件投递

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['WEBHOOK_SECRET']

操作步骤:
  1. 创建 push 和 MR 事件的 Webhook
  2. 触发 push 事件
  3. 验证接收端收到请求且签名正确

预期结果:
  1. Webhook 创建成功
  2. 事件投递到达
  3. 签名可验证

验证点:
  - [正向] Webhook 创建成功
  - [正向] URL 正确

清理:      fixture
