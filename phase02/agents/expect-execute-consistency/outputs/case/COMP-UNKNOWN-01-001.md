# COMP-UNKNOWN-01-001
- **标题**: 包含未知顶层字段的 workflow 触发 YAML 校验失败   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: validation_failed | COVERED | 校准8: malformed YAML/unknown_field 校验失败 |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT | R5 |
