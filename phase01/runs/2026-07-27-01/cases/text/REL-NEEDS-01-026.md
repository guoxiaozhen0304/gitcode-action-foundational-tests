用例 ID:   REL-NEEDS-01-026
维度标签:   [reliability, completeness]
维度:      稳定性
优先级:    P0
溯源意图:  INTENT-REL-069
参照来源:  history/issues-encountered.md #101; baseline/risk-register.md RISK-REL-02
母意图:    —
标题:      needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行

前置条件:
  - fixture 仓库可提交并触发 workflow
  - 历史实证 bug #101（★）：jobA needs matrix jobB，jobB 成功后 jobA 仍初始化失败

操作步骤:
  1. 提交 workflow：jobB 为 3 实例 matrix（fail-fast=false，全部实例设计为成功），jobA 通过 needs 依赖 jobB 且不附加任何 if 条件
  2. 手动触发该 workflow，观察 jobB 各实例与 jobA 的状态流转
  3. 在 jobA 内读取并输出 needs.jobB.result 聚合值

预期结果:
  - jobB 的 3 个 matrix 实例全部 success
  - jobA 正常初始化、进入执行并 completed(success)
  - jobA 内 needs.jobB.result 求值为 success

验证点:
  - [正向] jobB 全部 matrix 实例状态=success
  - [正向] jobA 状态=success，日志中含 needs.jobB.result=success
  - [负向] jobA 不应在 jobB 全成功时初始化失败或状态=skipped（#101 回归点；复现即 blocker）
  - [非功能] jobB 末实例完成到 jobA 启动的聚合判定延迟 ≤120 秒

清理:      无需重置（仅状态观测，无破坏性副作用）
