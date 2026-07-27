用例 ID:   SEC-ORG-01-001
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-039
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/security-knowledge/issues.md §1/§2
母意图:    —
标题:      可见范围外仓库的 workflow 绝不应读到组织级 secret 原值

前置条件:
  - 组织级 secret ORG_SHARED_KEY（占位值）已创建，可见范围仅包含仓库 A
  - fixture 仓库 B 同属该组织但不在可见范围内

操作步骤:
  1. 在仓库 B 触发 workflow，引用 ORG_SHARED_KEY 并输出
  2. 在仓库 A 触发同样 workflow 作为对照
  3. 变更可见性配置后立即重跑仓库 B 的 workflow，观察生效时延

预期结果:
  - 仓库 A（范围内）正常引用
  - 仓库 B（范围外）引用返回空或报错，日志全文搜索原值命中数为 0
  - 可见性配置变更即时生效，无缓存残留窗口

验证点:
  - [正向] 范围内仓库可正常引用组织级 secret
  - [负向] 范围外仓库的 workflow 绝不应读到组织级 secret 原值
  - [非功能] 可见性配置变更即时生效（无缓存残留窗口）

清理:      重置 fixture 仓库
