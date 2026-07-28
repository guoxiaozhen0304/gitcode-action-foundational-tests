# COMPAT-OUTCOME-01-003

- **标题**: outcome 与 conclusion 在 job 条件判断中不应互换语义   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | job_status | positive | ==success | COVERED | llm_assisted (LLM→断言一致) |
| 2 | step_status | positive | ==failure | COVERED | llm_assisted (LLM→断言一致) |
| 3 | semantic_swap | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
