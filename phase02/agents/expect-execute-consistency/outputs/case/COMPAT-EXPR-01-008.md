# COMPAT-EXPR-01-008

- **标题**: toJson 表达式输出格式差异（pretty-print vs compact）   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | key1 | COVERED |  |
| 2 | run_logs | nonfunctional | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
