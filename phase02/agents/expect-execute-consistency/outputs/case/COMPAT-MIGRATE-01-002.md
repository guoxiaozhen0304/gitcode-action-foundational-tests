# COMPAT-MIGRATE-01-002

- **标题**: GitHub 风格 run-name 语法迁移报错应给出可操作指引   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | validation_error | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 2 | error_message | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
