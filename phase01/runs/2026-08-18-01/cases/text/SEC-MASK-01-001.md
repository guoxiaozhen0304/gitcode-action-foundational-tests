用例 ID:   SEC-MASK-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-002
母意图:    —
标题:      secret 经过 JSON 转义与 URL 编码后仍应在日志中被掩码

前置条件:
  - 仓库 fixture: with-secrets
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 以 JSON 转义、URL 编码、逐字符拆分形式输出 secret
  2. 下载日志验证所有形式均被掩码

预期结果:
  1. 所有变形后的 secret 值均显示为 ***
  2. 日志中不应出现 DEPLOY_TOKEN 的任何变形值

验证点:
  - [负向] 日志不含 secret 变形值
  - [正向] workflow 完成

清理:      fixture
