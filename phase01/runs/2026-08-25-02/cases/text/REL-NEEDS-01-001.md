用例 ID:   REL-NEEDS-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P0
溯源意图:  INTENT-REL-005
母意图:    —
标题:      needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游不应执行

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发 workflow
  2. 验证 init job 失败后 matrix-job 被跳过
  3. 验证 downstream job 被跳过

预期结果:
  1. init job 失败
  2. matrix-job 状态为 skipped
  3. downstream 状态为 skipped

验证点:
  - [正向] init job 失败
  - [正向] matrix job 被跳过
  - [负向] downstream 未执行

清理:      fixture
