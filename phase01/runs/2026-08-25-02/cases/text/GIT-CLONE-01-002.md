用例 ID:   GIT-CLONE-01-002
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-GIT-001
母意图:    —
标题:      Git Clone 使用 PAT 进行 HTTPS 鉴权

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['PAT_TOKEN']

操作步骤:
  1. 使用含 PAT 的 HTTPS URL 执行 git clone
  2. 验证本地目录已创建且包含 .git

预期结果:
  1. clone 成功退出码为 0
  2. 本地目录包含有效 Git 仓库
  3. 日志或输出中不应出现 PAT 明文

验证点:
  - [正向] git clone 成功
  - [正向] 输出包含 clone 成功提示
  - [负向] 输出不含 PAT 明文

清理:      fixture
