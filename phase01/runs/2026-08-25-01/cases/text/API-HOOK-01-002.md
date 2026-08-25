用例 ID:   API-HOOK-01-002
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-HOOK-001
母意图:    —
标题:      Webhook 签名验证失败时拒绝请求

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 使用错误签名模拟 Webhook 回调
  2. 验证服务端拒绝或标记为无效

预期结果:
  1. 错误签名的请求不被信任

验证点:
  - [负向] 签名错误时返回非 200 或鉴权失败

清理:      fixture
