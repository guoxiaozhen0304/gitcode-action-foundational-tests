用例 ID:   SEC-FORK-01-002
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-001
母意图:    —
标题:      fork PR 通过 ${{ secrets }} 对象枚举不得获取 secret 名列表

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN', 'API_KEY']

操作步骤:
  1. 在 fork PR workflow 中尝试枚举 secrets
  2. 验证无法获取 secret 名称或值

预期结果:
  1. secrets 对象不可枚举
  2. 环境变量中无目标仓库 secrets

验证点:
  - [负向] 日志不含 DEPLOY_TOKEN 名称
  - [负向] 日志不含 API_KEY 名称

清理:      fixture
