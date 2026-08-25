用例 ID:   SEC-PERM-01-002
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-012
母意图:    —
标题:      job 级 permissions 声明应正确限制 ATOMGIT_TOKEN 权限

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 在 job 级别声明不同 permissions
  2. 验证 read-only job 无法执行写操作
  3. 验证 write-job 可执行写操作

预期结果:
  1. read-only job 的写操作被拒绝
  2. write-job 的写操作成功

验证点:
  - [正向] read-only job 写操作被拒绝
  - [正向] workflow 完成

清理:      fixture
