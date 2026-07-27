用例 ID:   SEC-PERM-01-003
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-017
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）

前置条件:
  - 仓库未配置 permissions 声明

操作步骤:
  1. 提交一个未声明 permissions 的 workflow
  2. 触发 workflow 并尝试执行写操作

预期结果:
  - 默认状态下 ATOMGIT_TOKEN 仅拥有仓库 read 权限
  - 写操作被平台拒绝，返回 HTTP 403（写接口成功响应码 201 绝不应出现）

验证点:
  - [负向] 默认状态下 ATOMGIT_TOKEN 绝不应拥有写权限（日志中绝不应出现写操作成功的 201 响应码）
  - [正向] 越权写操作日志中包含 403
  - [非功能] 默认权限应在组织级可配置为更严格（如 none）

清理:      重置 fixture 仓库
