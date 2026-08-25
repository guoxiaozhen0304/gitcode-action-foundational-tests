用例 ID:   COMPAT-PRTARGET-01-001
维度标签:   ['compatibility', 'security']
维度:      compatibility
优先级:    P0
溯源意图:  INTENT-COMPAT-024
母意图:    —
标题:      pull_request_target 默认 checkout 目标仓库 base 分支代码

前置条件:
  - 仓库 fixture: with-fork-pr
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. 在 pull_request_target 事件触发 workflow
  2. 检查 checkout 的代码来源
  3. 验证 origin 指向目标仓库而非 fork

预期结果:
  1. checkout 的 origin 是目标仓库
  2. workflow 文件来自 base 分支
  3. ATOMGIT_TOKEN 权限不升级

验证点:
  - [正向] checkout 来源为目标仓库
  - [负向] 日志不含 fork 仓库地址
  - [正向] workflow 运行完成

清理:      fixture
