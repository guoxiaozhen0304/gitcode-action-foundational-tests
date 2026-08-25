用例 ID:   COMPAT-PRTARGET-01-002
维度标签:   ['compatibility', 'security']
维度:      compatibility
优先级:    P0
溯源意图:  INTENT-COMPAT-024
母意图:    —
标题:      pull_request_target 中显式 checkout PR 头分支后执行不可信脚本应被隔离

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 在 pull_request_target 中 checkout PR 头分支
  2. 运行该分支中的构建脚本
  3. 验证 secret 仍被隔离或脚本在受限上下文执行

预期结果:
  1. 即使 checkout 了 PR 头分支，secret 仍不可读取
  2. 日志中 DEPLOY_TOKEN 被掩码

验证点:
  - [负向] 日志不含 secret 明文
  - [正向] workflow 运行完成

清理:      fixture
