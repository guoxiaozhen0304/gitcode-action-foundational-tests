用例 ID:   SEC-PRTARGET-01-002
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-007
母意图:    —
标题:      pull_request_target 中恶意 PR 修改 workflow 文件不被执行

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. fork PR 修改 workflow 文件试图泄露 secret
  2. 触发 pull_request_target
  3. 验证实际执行的 workflow 仍来自 base 分支

预期结果:
  1. 执行的 workflow 文件是 base 分支版本
  2. PR 中的修改未被加载

验证点:
  - [正向] 校验 workflow 文件
  - [负向] 无 secret 泄露

清理:      fixture
