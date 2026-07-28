# COMPAT-SCHEDULE-01-001
- **标题**: schedule cron 按 UTC 时间触发
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证schedule workflow的cron表达式按UTC时间解释，workflow能正常触发。

## 做了什么
workflow配置 `schedule cron: "0 12 * * *"`，step输出 `echo "SCHEDULE_TRIGGER_OK"` + `date -u +...` 输出当前UTC时间。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功执行 | COVERED | run_status平台可观测 |
| 2 | run_event | positive equals schedule | 运行事件为schedule | COVERED | run_event平台日志可观测(GENUINE R1)；事件类型为platform记录 |
| 3 | run_logs | nonfunctional llm | "触发时间应按UTC解释" | COVERED | date -u为真实命令(GENUINE R1)，输出当前UTC时间可观测；R5 LLM_DEPENDENT辅助判断但命令已产生证据 |
