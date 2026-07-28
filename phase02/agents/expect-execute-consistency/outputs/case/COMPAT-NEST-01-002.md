# COMPAT-NEST-01-002

- **标题**: workflow_call 嵌套层数 - 3 层越界应报错   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | ==success | COVERED | ; expects run to fail (genuine negative) |
| 2 | error_message | nonfunctional | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
