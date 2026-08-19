用例 ID:   SEC-RUNNER-01-002
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-020
母意图:    —
标题:      自托管 Runner 注册令牌不得在工作流日志或环境变量中泄露

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['RUNNER_REGISTRATION_TOKEN']

操作步骤:
  1. 在自托管 runner 上执行 workflow
  2. 检查日志和环境变量输出
  3. 验证注册令牌不出现

预期结果:
  1. 日志中不含 RUNNER_REGISTRATION_TOKEN
  2. 环境变量中不含注册令牌

验证点:
  - [负向] 日志不含注册令牌
  - [正向] workflow 完成

清理:      fixture
