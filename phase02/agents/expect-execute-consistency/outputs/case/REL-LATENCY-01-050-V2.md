# REL-LATENCY-01-050-V2
- **标题**: 调度延迟压力——并发 20 个 job 的排队延迟与完成率
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
并发触发 20 个单 job workflow（各 sleep 60s），验证 20 个 job 全部完成、无饿死、排队延迟可观测。
## 做了什么
YAML 使用 matrix index [1..20] 触发 20 个并行 job（single workflow 内），各 sleep 60。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_jobs_count | positive | equals 20 | COVERED | YAML sleep 60 真实命令 + matrix 20 实例，platform 日志确认全部完成 |
| 2 | max_queued_time_seconds | nonfunctional | le 300 | COVERED | YAML assert 最大排队时间 ≤300s，排队延迟可观测 |
| 3 | no_starvation | negative | 无 job 被无限饿死 | COVERED | completed_jobs_count=20 + max_queued ≤300s 隐含无饿死，对应文本负向断言 |
