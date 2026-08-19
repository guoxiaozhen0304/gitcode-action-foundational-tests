用例 ID:   API-REPO-01-002
维度标签:   ['completeness']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-GIT-005
母意图:    —
标题:      空仓库的分支列表返回空数组

前置条件:
  - 仓库 fixture: empty-repo

操作步骤:
  1. 对空仓库调用分支列表 API

预期结果:
  1. 返回 200
  2. 分支列表为空数组

验证点:
  - [正向] 空仓库返回 200
  - [正向] 分支列表为空数组

清理:      fixture
