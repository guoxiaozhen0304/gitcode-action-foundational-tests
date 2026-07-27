用例 ID:   REL-NEEDS-01-027
维度标签:   [reliability, completeness]
维度:      稳定性
优先级:    P0
溯源意图:  INTENT-REL-069
参照来源:  history/issues-encountered.md #101; baseline/risk-register.md RISK-REL-02
母意图:    REL-NEEDS-01-026（变体：matrix 1 实例失败、fail-fast=false 时的聚合判定）
标题:      needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行

前置条件:
  - fixture 仓库可提交并触发 workflow
  - 与 REL-NEEDS-01-026 同一 needs×matrix 聚合判定面（成功路径互补）

操作步骤:
  1. 提交 workflow：jobB 为 3 实例 matrix（fail-fast=false），其中 1 个实例设计为失败、其余 2 个成功
  2. jobA 通过 needs 依赖 jobB 且不附加任何 if 条件
  3. 手动触发，观察 jobB 全部实例终态与 jobA 的聚合判定结果

预期结果:
  - jobB 失败实例数=1、成功实例数=2（fail-fast=false 不取消其余实例）
  - jobB 聚合结果=failure，jobA 状态=skipped 且不执行其 step

验证点:
  - [正向] jobB 聚合状态=failure，失败实例数=1、成功实例数=2
  - [正向] jobA 状态=skipped
  - [负向] jobA 不应在 jobB 部分失败时被执行（状态≠success，step 不产出日志）
  - [负向] fail-fast=false 下其余 2 个实例不应被中途取消

清理:      无需重置（仅状态观测，无破坏性副作用）
