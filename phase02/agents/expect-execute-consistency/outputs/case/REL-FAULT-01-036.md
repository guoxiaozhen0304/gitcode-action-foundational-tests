# REL-FAULT-01-036
- **标题**: 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
runner→平台方向网络分区 60s 后恢复，验证 job 续跑完成（status=success，日志含 post_partition_marker），分区窗口内不应判 failure/cancelled，记录心跳判死阈值。
## 做了什么
YAML 定义 4 个 step（pre/long work 180s/post/final marker），fault_injection network_partition scope runner_to_platform duration 60s at step 2。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals success | COVERED | YAML sleep 180 真实命令 + fault_injection，platform 日志确认分区恢复后续跑成功 |
| 2 | run_logs | positive | contains post_partition_marker | COVERED | YAML echo "post_partition_marker" → GENUINE（非 VACUOUS 因为分区恢复后执行，有真实意义） |
| 3 | job_status | negative | equals failure | COVERED | YAML 负向断言 job ≠ failure，对应文本"分区 60 秒窗口内 job 不应被判 failure" |
| 4 | heartbeat_death_threshold_observation | nonfunctional | equals recorded | COVERED | YAML assert 心跳判死阈值记录，对应文本"平台实际心跳判死阈值线索记录" |
