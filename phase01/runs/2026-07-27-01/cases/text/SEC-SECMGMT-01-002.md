用例 ID:   SEC-SECMGMT-01-002
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-038
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/security-knowledge/issues.md §2
母意图:    —
标题:      无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合

前置条件:
  - fixture 仓库已存在 secret DEPLOY_TOKEN（占位值）
  - 存在无 secret 管理权限的测试成员角色

操作步骤:
  1. 以无权限角色身份分别尝试创建新 secret、更新 DEPLOY_TOKEN、删除 DEPLOY_TOKEN
  2. 记录各操作响应码
  3. 操作后以管理员身份核对 secret 集合与 DEPLOY_TOKEN 值未变化

预期结果:
  - 三类越权操作全部返回 403
  - secret 集合与值保持不变
  - 审计断言挂靠 SEC-AUDIT-01-001（本条不重复展开）

验证点:
  - [正向] 授权管理员同类管理操作成功
  - [负向] 无权限角色的管理操作绝不应成功，且 secret 集合绝不应被改变

清理:      重置 fixture 仓库
