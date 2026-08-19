用例 ID:   SEC-PERM-01-001
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-011
母意图:    —
标题:      未声明 permissions 时 ATOMGIT_TOKEN 默认权限应只读

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 在不含 permissions 声明的 workflow 中使用 ATOMGIT_TOKEN
  2. 验证默认权限范围
  3. 验证删除等写操作被拒绝

预期结果:
  1. ATOMGIT_TOKEN 默认可读取用户/仓库信息
  2. 删除仓库等高危操作返回 403

验证点:
  - [正向] 读取操作成功
  - [正向] 删除操作被拒绝
  - [正向] workflow 完成

清理:      fixture
