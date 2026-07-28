# COMPAT-PR-01-003

- **标题**: PR types 配置后匹配类型不触发与 GitHub 行为差异   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 2 | run_status | positive | ==success | COVERED | llm_assisted (LLM→断言一致) |
