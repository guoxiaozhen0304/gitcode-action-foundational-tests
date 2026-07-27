用例 ID:   SEC-DEFPERM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-036
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

前置条件:
  - 仓库未声明或声明了部分 permissions

操作步骤:
  1. 提交一个 workflow，顶层声明 repository: read，job 级覆盖为 repository: write
  2. 触发 workflow 并验证实际权限

预期结果:
  - 顶层声明被各 job 继承
  - job 级声明覆盖顶层
  - 越权写操作返回 HTTP 403（写接口成功的 201 绝不应出现）

验证点:
  - [正向] 顶层声明被各 job 继承；job 级声明覆盖顶层（override-write job 声明 repository: write 后读操作返回 READ_200）；越权写操作的响应码包含 WRITE_403
  - [负向] 不应发生：实际权限宽于声明范围（未声明的权限域不应因覆盖关系被隐式放大；日志中绝不应出现写操作成功的 201 响应码）
  - [非功能] 权限范围与覆盖关系可被观测判定（HTTP 响应码为可观测判据）

清理:      重置 fixture 仓库
