# COMPAT-EXPR-01-016

- **标题**: format() 花括号转义与字符串字面量引号规则边界   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | PROBE_DONE | COVERED |  |
| 2 | run_logs | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 3 | run_logs | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
