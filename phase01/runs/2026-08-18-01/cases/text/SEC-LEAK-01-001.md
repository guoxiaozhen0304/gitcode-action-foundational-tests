用例 ID:   SEC-LEAK-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-003
母意图:    —
标题:      secret 值不得通过 artifact 文件外泄

前置条件:
  - 仓库 fixture: with-secrets
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 将 secret 写入文件并作为 artifact 上传
  2. 下载 artifact 验证内容
  3. 验证 secret 是否被平台拦截或掩码

预期结果:
  1. artifact 中 secret 被掩码或上传被阻止
  2. 下载后的文件内容为 *** 或空

验证点:
  - [负向] artifact 不含 secret 明文
  - [正向] workflow 完成

清理:      fixture
