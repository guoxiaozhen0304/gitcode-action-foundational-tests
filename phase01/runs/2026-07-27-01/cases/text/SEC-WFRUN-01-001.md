用例 ID:   SEC-WFRUN-01-001
维度标签:   [security, compatibility]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-044
参照来源:  inputs/gitcode-spec（全库无 workflow_run）; inputs/security-knowledge/github-actions-security-series.md Part 1/4
母意图:    —
标题:      不可信运行绝不应存在隐式拉起高权限后续运行的链式路径

前置条件:
  - fixture 仓库存在一个已完成的 fork PR 运行
  - harness 可枚举平台可用触发器清单与运行列表

操作步骤:
  1. 枚举平台可用触发器清单，确认无 workflow_run 等价机制（与 INTENT-COMPAT-037 事件降级面共享证据链）
  2. fork PR 运行结束后，检索其后是否自动拉起任何携带 secrets/写权限的特权运行
  3. 检索文档是否明示 workflow_run 不支持及替代安全模式

预期结果:
  - 触发器清单中无 workflow_run 等价物
  - fork PR 运行结束后无任何自动拉起的特权运行记录
  - 文档明示不支持及替代模式（如 pull_request_target + 审批/label gate）

验证点:
  - [负向] 不可信（fork PR）运行绝不应隐式拉起高权限后续运行
  - [非功能] 文档应明示 workflow_run 不支持及替代安全模式（llm 辅助判定）

清理:      无需重置（只读观测，无副作用）
