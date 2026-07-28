# COMPAT-SCHEDULE-01-002
- **标题**: schedule 不支持 timezone 字段差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 对不支持的 schedule timezone 字段的行为——应给出明确校验错误或文档说明忽略策略，不应导致不可预期行为。
## 做了什么
提交含 `schedule.timezone: "Asia/Shanghai"` 字段的工作流，观察平台校验行为。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=success（不应成功） | COVERED | Harness 可直接检查运行状态，若成功则为负面发现 |
| 2 | error_message | nonfunctional | llm_assisted 判断报错信息明确 | LLM_DEPENDENT | type=nonfunctional，需人工阅读报错内容 |
