用例 ID:   COMPAT-MASK-01-001
维度标签:   ['compatibility', 'security']
维度:      compatibility
优先级:    P0
溯源意图:  INTENT-COMPAT-023
母意图:    —
标题:      secret 经过 base64 拼接变形后仍应在日志中被掩码

前置条件:
  - 仓库 fixture: with-secrets
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 在 workflow 中以 base64、拼接、多行形式输出 secret
  2. 下载 job 日志检查是否被掩码

预期结果:
  1. 日志中所有变形后的 secret 值均显示为 ***
  2. 不应出现 DEPLOY_TOKEN 明文或其 base64 值

验证点:
  - [负向] 日志不含 secret 明文
  - [正向] workflow 运行完成

清理:      fixture
