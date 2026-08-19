用例 ID:   REL-MATX-01-002
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-007
母意图:    —
标题:      matrix fail-fast=true 时单实例失败取消其余实例

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发含 fail-fast=true 的矩阵 workflow
  2. 其中一个实例失败
  3. 验证其余实例被取消

预期结果:
  1. 失败实例状态为 failure
  2. 其余实例状态为 cancelled 或 skipped
  3. 整体 workflow 状态为 failure

验证点:
  - [正向] 失败实例标记为 failure
  - [正向] 其余实例被取消
  - [正向] 整体状态为 failure

清理:      fixture
