# COMPAT-MATRIX-01-004

- **标题**: matrix include 无基础变量不被支持时的差异   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 2 | run_status | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
