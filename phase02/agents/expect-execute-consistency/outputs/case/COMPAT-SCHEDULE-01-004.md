# COMPAT-SCHEDULE-01-004
- **标题**: schedule 生命周期语义确认
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
确认GitCode schedule的自动停用/保活策略，并评估触发延迟可观测性（对照GitHub的60天无活动自动停用）。

## 做了什么
workflow配置 `schedule cron: "*/5 * * * *"`（每5分钟），step输出 `date -u +"ACTUAL_TRIGGER_UTC=..."` + `echo "SCHEDULE_PROBE_DONE"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "SCHEDULE_PROBE_DONE" | COVERED | echo直接覆盖(R1 GENUINE) |
| 2 | run_list | negative llm | "长期观察窗口内不应出现未文档化的静默停用" | COVERED | run_list长期可观测(R1平台日志)；date -u为真实命令(GENUINE) |
| 3 | run_list | nonfunctional llm | "比对计划时间与实际入队时间，延迟可观测" | COVERED | date -u输出(GENUINE R1)与cron计划时间可对比；R5 LLM辅助比对但证据已在日志 |
