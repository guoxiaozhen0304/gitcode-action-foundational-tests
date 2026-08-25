用例 ID:   SEC-HOOK-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-018
母意图:    —
标题:      Webhook secret 在配置界面不回显且签名验证不可绕过

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['WEBHOOK_SECRET']

操作步骤:
  1. 获取 Webhook 列表
  2. 验证响应中 secret 字段被掩码
  3. 使用错误签名调用验证被驳回

预期结果:
  1. secret 字段显示为 *** 或省略
  2. 错误签名请求被拒绝

验证点:
  - [正向] 获取列表成功
  - [负向] 响应不含 secret 明文

清理:      fixture
