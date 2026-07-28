# REL-QUEUE-01-003
- **标题**: concurrency QUEUE 策略——超上限运行应排队等待   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 concurrency.max=2, exceed-action=QUEUE 时，超过上限的触发应排队等待而非丢弃。
## 做了什么
同时触发 4 次 workflow（每 job sleep 30s），验证前 2 个运行后 2 个排队，最终 4 个全部完成。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | 平台 API 查询最终运行状态 |
| 2 | queued_count | nonfunctional | equals "2" | COVERED | harness 统计排队运行的个数 |
