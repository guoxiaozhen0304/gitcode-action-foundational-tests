# COMP-TIMEOUT-01-001
- **标题**: 未声明 timeout-minutes 的 job 在 360 分钟内正常完成   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供；sleep 5 远小于360min |
| 2 | run_duration | nonfunctional | less_than_minutes: 360 | LLM_DEPENDENT | R5 |
