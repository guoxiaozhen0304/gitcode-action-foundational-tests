用例 ID:   SEC-PRTARGET-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-007
母意图:    —
标题:      pull_request_target 中 checkout PR 头分支后运行 build.sh 应被隔离

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 在 pull_request_target 中 checkout PR 头分支
  2. 运行该分支中的 build.sh
  3. 验证 secret 仍被隔离

预期结果:
  1. 即使 checkout 了 PR 头分支，DEPLOY_TOKEN 仍被掩码或为空
  2. build.sh 中的恶意代码无法获取 secrets

验证点:
  - [负向] 日志不含 secret 明文
  - [正向] workflow 完成

清理:      fixture
