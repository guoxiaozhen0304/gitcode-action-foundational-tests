用例 ID:   SEC-INJ-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-004
母意图:    —
标题:      PR 标题含命令注入 payload 时不应执行

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建 PR 标题含恶意命令注入 payload（如 `; cat /etc/passwd`）
  2. 触发 workflow
  3. 验证命令未被执行
  4. 验证日志中标题原样输出

预期结果:
  1. /etc/passwd 未被读取
  2. PR 标题作为纯文本输出

验证点:
  - [负向] 未执行注入命令
  - [正向] PR 标题原样输出
  - [正向] workflow 正常完成

清理:      fixture
