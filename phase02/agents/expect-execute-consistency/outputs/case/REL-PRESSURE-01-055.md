# REL-PRESSURE-01-055
- **标题**: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证并发压力下 concurrency 排队机制：max=5 时同时触发 20 次，running 峰值 ≤5，20 次全部完成，总耗时 ≤900 秒。
## 做了什么
在 10s 内并发触发 20 次同一 workflow（每 job sleep 30s），concurrency.max=5, exceed-action=QUEUE。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count | positive | equals "20" | COVERED | harness 统计全部进入终态的 run 数 |
| 2 | max_running_count | nonfunctional | le "5" | COVERED | harness 轮询状态统计峰值并发 |
| 3 | total_duration_seconds | nonfunctional | le "900" | COVERED | harness 测量从首次触发到最后一次终态的总耗时 |
