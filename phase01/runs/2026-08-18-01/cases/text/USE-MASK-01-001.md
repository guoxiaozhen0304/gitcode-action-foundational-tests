用例 ID:   USE-MASK-01-001
维度标签:   ['usability', 'security']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-011
母意图:    —
标题:      Secret 掩码被绕过时日志应发出暴露预警

前置条件:
  - 仓库 fixture: with-secrets
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 尝试以变形方式输出 secret
  2. 检查日志是否包含暴露预警
  3. 验证预警信息清晰可理解

预期结果:
  1. 若掩码被绕过，日志中应出现警告标识
  2. 警告提示用户 secret 可能已泄露

验证点:
  - [正向] 存在暴露预警
  - [正向] workflow 完成

清理:      fixture
