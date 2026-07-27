用例 ID:   SEC-SECMGMT-01-001
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-038
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/security-knowledge/issues.md §2
母意图:    —
标题:      Secret 写入后任何 API/UI 路径绝不应回读明文

前置条件:
  - 管理员已在 fixture 仓库创建 secret DEPLOY_TOKEN（占位值）

操作步骤:
  1. 枚举 secret 管理面的读取类 API 与 UI 响应（列表、详情等）
  2. 检查各响应中是否出现明文 value 字段
  3. 触发一个正常引用 DEPLOY_TOKEN 的 workflow，确认引用侧可用且日志脱敏

预期结果:
  - 任何读取接口/UI 均不返回 secret 明文（仅能更新覆盖）
  - workflow 正常引用该 secret，日志中显示为脱敏形式

验证点:
  - [正向] 授权管理员可创建/更新 secret，workflow 正常引用且日志脱敏
  - [负向] 任何读取接口/UI 绝不应返回 secret 明文

清理:      重置 fixture 仓库
