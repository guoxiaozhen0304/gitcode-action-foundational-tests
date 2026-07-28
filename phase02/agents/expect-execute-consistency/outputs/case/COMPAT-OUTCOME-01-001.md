# COMPAT-OUTCOME-01-001

- **标题**: continue-on-error false 时 outcome 与 conclusion 应均为 failure   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | step_status | positive | ==failure | COVERED | llm_assisted (LLM→断言一致) |
| 2 | step_conclusion | positive | ==failure | COVERED | llm_assisted (LLM→断言一致) |
| 3 | run_status | positive | ==failure | COVERED | llm_assisted (LLM→断言一致) |
