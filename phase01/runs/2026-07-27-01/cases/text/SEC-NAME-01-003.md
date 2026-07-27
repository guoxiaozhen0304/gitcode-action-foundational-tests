用例 ID:   SEC-NAME-01-003
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-041
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/history/issues-encountered.md #38
母意图:    —
标题:      可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒

前置条件:
  - 管理员身份可操作 secret 管理面

操作步骤:
  1. 分别尝试创建以下命名的 secret：ATOMGIT_TOKEN（系统前缀）、my-secret（含中划线）、1SECRET（数字开头）
  2. 记录各创建请求的响应与报错内容
  3. 创建合法命名 DEPLOY_KEY 作为对照

预期结果:
  - 三类违规命名全部被拒绝，返回明确校验错误
  - 合法命名创建成功
  - 报错指明命名规则（报错质量判定关联 INTENT-USE-028，共享证据链）

验证点:
  - [正向] 合法命名创建成功
  - [负向] 以 ATOMGIT_ 开头、含非法字符、数字开头的 secret 创建绝不应成功
  - [非功能] 拒绝时报错应指明命名规则（llm 辅助判定，关联 USE-028）

清理:      重置 fixture 仓库
