# COMP-SCHEDULE-01-003
- **标题**: cron 间隔短于 5 分钟时被拒绝或降级   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals: success_with_1min_interval | COVERED | cron */1 短于5min，不应成功 |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT | R5 |
