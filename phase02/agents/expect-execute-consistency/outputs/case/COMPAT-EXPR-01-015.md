# COMPAT-EXPR-01-015

- **标题**: startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | ==success | COVERED |  |
| 2 | run_logs | positive | PROBE_DONE | COVERED |  |
| 3 | run_logs | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
