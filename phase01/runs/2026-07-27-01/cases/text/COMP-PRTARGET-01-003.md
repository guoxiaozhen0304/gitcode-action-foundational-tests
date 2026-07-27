用例 ID:   COMP-PRTARGET-01-003
维度标签:   [completeness, security]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-023
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/core-concepts/trigger-events.md; security-permissions/pr-mr-pipeline-security.md
母意图:    —
标题:      fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查

前置条件:
  - 仓库已启用 AtomGit Action
  - 仓库配置 TEST_SECRET 占位 secret
  - 存在来自 fork 仓库的 PR（不可信贡献者）

操作步骤:
  1. 按 core-concepts/trigger-events.md 的推荐编写 on.pull_request_target 的 workflow，checkout PR head.sha
  2. 以 fork PR 触发，观察 secrets 是否注入、平台是否给出安全警示
  3. 逐字记录事实，为文档冲突收敛提供底座

预期结果:
  - 平台层事实被确定：fork PR 在 pull_request_target 下的 secrets 注入行为与警示情况逐字记录；secret 明文不落入日志；矛盾文档清单回写 Parity Matrix

验证点:
  - [负向] secret 明文不应出现在任何日志中
  - [负向] 按推荐配置不应在无平台警示的情况下默认获得 secrets 与写权限（记录实际行为）
  - [正向] base 分支 workflow 版本约束实测成立（复用 INTENT-COMP-014 证据链）

清理:      重置 fixture 仓库（含关闭 fork PR）
