# COMPAT-SCHEDULE-01-001
- **标题**: schedule cron 按 UTC 时间触发
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 schedule cron workflow 按 UTC 时间触发，确认时区解释行为。
## 做了什么
提交含 `schedule.cron` 表达式的工作流，等待或模拟触发时刻，检查触发时间。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success | COVERED | 标准运行状态检查 |
| 2 | run_event | positive | equals=schedule | COVERED | 事件类型检查，与 trigger.event=schedule 一致 |
| 3 | run_logs | nonfunctional | llm_assisted 判断触发时间UTC一致性 | LLM_DEPENDENT | type=nonfunctional，需人工比对时间 |
