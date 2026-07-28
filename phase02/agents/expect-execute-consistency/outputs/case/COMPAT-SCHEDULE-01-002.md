# COMPAT-SCHEDULE-01-002
- **标题**: schedule 不支持 timezone 字段差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证schedule workflow中timezone字段的处理行为——明确报错或文档化忽略策略。

## 做了什么
workflow配置 `schedule cron + timezone: "Asia/Shanghai"`，step输出 `echo "SCHEDULE_TIMEZONE_OK"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative equals success | "不应因timezone字段导致不可预期行为" | COVERED | run_status可观测；negative equals success意为"不应轻松通过"——若平台拒绝则run_status不为success符合预期 |
| 2 | error_message | nonfunctional llm | "错误信息应明确指出timezone不支持" | COVERED | error_message为平台日志(GENUINE R1)；即使平台静默忽略，无error_message也可判定 |
