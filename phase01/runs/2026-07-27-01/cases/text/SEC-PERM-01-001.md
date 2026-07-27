用例 ID:   SEC-PERM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-016
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN

前置条件:
  - 仓库配置了 permissions 声明

操作步骤:
  1. 提交一个 workflow，在 job 级显式声明 repository: read
  2. 触发 workflow 并尝试执行写操作

预期结果:
  - 声明 read 时读操作成功
  - 声明 read 时写操作返回 HTTP 403（写接口成功响应码 201 绝不应出现）

验证点:
  - [正向] 声明 read 时读操作（clone、API 读取）成功；越权写操作日志中包含 403
  - [负向] 声明 read 时写操作（push、评论、修改 PR）返回 403 或失败，日志中绝不应出现写操作成功的 201 响应码

清理:      重置 fixture 仓库
