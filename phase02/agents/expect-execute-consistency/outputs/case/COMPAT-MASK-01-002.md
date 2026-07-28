# COMPAT-MASK-01-002

- **标题**: 通过 env 注入 secret 后输出应在日志中被脱敏   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | !secret[TEST_SECRET] | COVERED |  |
| 2 | run_logs | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 3 | run_status | positive | ==success | COVERED | llm_assisted (LLM→断言一致) |
