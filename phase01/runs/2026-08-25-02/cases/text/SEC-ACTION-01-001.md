用例 ID:   SEC-ACTION-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-014
母意图:    —
标题:      浮动 tag 被篡改后使用 commit SHA 固定可防供应链攻击

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 验证平台支持通过 commit SHA 固定 action 版本
  2. 验证浮动 tag 可被重定向

预期结果:
  1. commit SHA 引用成功
  2. 浮动 tag 引用也成功但存在被篡改风险（已记录）

验证点:
  - [正向] workflow 完成

清理:      none
