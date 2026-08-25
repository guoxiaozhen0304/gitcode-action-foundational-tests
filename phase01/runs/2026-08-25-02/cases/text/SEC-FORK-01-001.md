用例 ID:   SEC-FORK-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-001
母意图:    —
标题:      fork PR 触发 pull_request 时严禁读取目标仓库 secrets

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 以外部 fork 贡献者身份提交试图输出 DEPLOY_TOKEN 的 workflow
  2. 在 fork PR 场景下触发
  3. 验证 secret 不可访问且日志被掩码

预期结果:
  1. fork PR workflow 中 secrets.DEPLOY_TOKEN 为空或被掩码
  2. 运行日志中不出现 DEPLOY_TOKEN 明文

验证点:
  - [负向] 日志不含 secret 明文
  - [正向] workflow 运行完成
  - [负向] fork 身份无 secret 访问权限

清理:      fixture
