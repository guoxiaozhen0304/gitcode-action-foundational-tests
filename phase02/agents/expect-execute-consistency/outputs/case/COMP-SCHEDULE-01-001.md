# COMP-SCHEDULE-01-001
- **标题**: 合法 cron 在默认分支按时触发   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 |
| 2 | run_event | positive | equals: schedule | COVERED | 平台提供；R3: 匹配 trigger.event=schedule |
| 3 | run_logs | positive | must_contain: SCHEDULED_RUN_UTC= | COVERED | step echo SCHEDULED_RUN_UTC=$(date) |
| 4 | trigger_time | nonfunctional | eval: llm_assisted | LLM_DEPENDENT | R5 |
