# COMPAT-EXPR-01-010

- **标题**: loose equality null 与空字符串及零的等价性差异   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | NULL_EQ_EMPTY= | COVERED |  |
| 2 | run_logs | positive | NULL_EQ_ZERO= | COVERED |  |
| 3 | run_logs | nonfunctional | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
