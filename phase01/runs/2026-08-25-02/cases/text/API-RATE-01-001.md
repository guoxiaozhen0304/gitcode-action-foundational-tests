用例 ID:   API-RATE-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-018
母意图:    —
标题:      高频触发下 API 正确返回 429 与 Retry-After

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 以高频（如 1000 QPS）调用仓库详情 API
  2. 观察返回状态码
  3. 验证 429 与 Retry-After 头

预期结果:
  1. 超过阈值后返回 429
  2. 响应头含 Retry-After
  3. 未返回 500 等内部错误

验证点:
  - [正向] 返回 429
  - [正向] 含 Retry-After 头

清理:      none
