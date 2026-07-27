用例 ID:   REL-FAULT-01-036
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-080
参照来源:  testing-focus.md §12 稳定性专项; platform-config/instance-config.md
母意图:    —
标题:      故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败

前置条件:
  - 具备故障注入能力（runner 出站方向对平台的网络分区）
  - fixture 仓库可接受破坏性测试
  - 平台心跳判死阈值未公开（本组顺带观测）

操作步骤:
  1. 触发含 4 个 step 的 workflow，在第 2 个 step 执行中注入 runner→平台方向网络分区，持续 60 秒
  2. 分区恢复后继续观察 job 至终态
  3. 校验日志在分区前后连续（含分区后标记行）

预期结果:
  - 分区 60 秒恢复后 job 继续执行并成功完成
  - 分区窗口内平台不得误判 job 为 failure/cancelled
  - 日志含分区前后的连续输出

验证点:
  - [正向] job 终态=success，日志含分区后标记行
  - [负向] 分区 ≤60 秒窗口内 job 不应被判 failure/cancelled
  - [非功能] 平台实际心跳判死阈值线索（首次误判时间点，若出现）记录并回写 platform-config

恢复预期:  自动恢复（网络恢复后 job 续跑完成；若超阈值失败则 rerun 应成功）
清理:      重置 fixture 仓库
