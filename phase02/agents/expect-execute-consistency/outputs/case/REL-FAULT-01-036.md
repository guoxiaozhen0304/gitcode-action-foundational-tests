# REL-FAULT-01-036
- **标题**: 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
runner→平台分区 60s 恢复后 job 续跑 success，不误判 failure/cancelled。

## 做了什么
4 step job（pre_marker→sleep 180s→post_marker→final_marker）；fault_injection 在 step 2 注入 60s 分区。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | 60s 分区恢复后 job 续跑完成，状态可观测 |
| 2 | run_logs | positive | contains "post_partition_marker" | COVERED | post_marker 在分区恢复后执行，echo 输出可观测 |
| 3 | job_status | negative | equals "failure" | COVERED | 60s 不应被判 failure |
| 4 | heartbeat_death_threshold_observation | nonfunctional | equals "recorded" | LLM_DEPENDENT | 观测记录型指标 |
