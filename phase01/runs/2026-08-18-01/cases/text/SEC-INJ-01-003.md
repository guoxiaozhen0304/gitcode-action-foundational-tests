用例 ID:   SEC-INJ-01-003
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-005
母意图:    —
标题:      issue_comment 正文含脚本注入 payload 时不应执行

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 创建 issue comment 含恶意 payload
  2. 触发 workflow
  3. 验证命令未被执行

预期结果:
  1. comment 正文作为纯文本输出
  2. 无命令注入执行

验证点:
  - [负向] 未执行注入命令
  - [正向] workflow 正常完成

清理:      fixture
