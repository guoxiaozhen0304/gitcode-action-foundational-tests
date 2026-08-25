用例 ID:   USE-PKG-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P2
溯源意图:  INTENT-USE-009
母意图:    —
标题:      制品库版本冲突报错应包含包名、版本号与操作指引

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 上传已存在的包版本
  2. 验证返回 409
  3. 验证错误信息包含包名、版本号与解决指引

预期结果:
  1. 返回 409 Conflict
  2. 错误信息包含 existing-pkg、1.0.0
  3. 提示 bump version 或使用 force

验证点:
  - [正向] 返回 409
  - [正向] 错误包含版本号
  - [正向] 错误包含包名

清理:      none
