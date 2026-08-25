用例 ID:   GIT-CLONE-01-003
维度标签:   ['completeness', 'security']
维度:      completeness
优先级:    P0
溯源意图:  INTENT-GIT-001
母意图:    —
标题:      Git Clone 使用 SSH 密钥鉴权

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 配置 SSH 密钥后执行 git clone

预期结果:
  1. clone 成功退出码为 0
  2. 本地目录包含有效 Git 仓库

验证点:
  - [正向] git clone 成功
  - [正向] 输出包含 clone 成功提示

清理:      fixture
