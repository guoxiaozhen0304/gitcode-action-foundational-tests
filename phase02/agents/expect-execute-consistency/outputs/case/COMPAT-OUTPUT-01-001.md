# COMPAT-OUTPUT-01-001

- **标题**: 跨 Job 引用未声明 output 时返回空值的差异   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | ==success | COVERED | llm_assisted (LLM→断言一致) |
| 2 | run_logs | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
