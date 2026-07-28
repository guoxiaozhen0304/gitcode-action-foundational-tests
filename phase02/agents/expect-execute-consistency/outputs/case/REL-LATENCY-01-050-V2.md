# REL-LATENCY-01-050-V2
- **标题**: 调度延迟压力——并发 20 个 job 的排队延迟与完成率
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
20 个并发 job 全部完成，无饿死，排队延迟可观测。

## 做了什么
matrix 20 实例，各 sleep 60s。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_jobs_count | positive | equals "20" | COVERED | matrix 20 实例全部执行完成 |
| 2 | max_queued_time_seconds | nonfunctional | le 300 | LLM_DEPENDENT | 非功能延迟指标，需 harness 测量 |
