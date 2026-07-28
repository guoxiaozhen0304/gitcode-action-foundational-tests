# COMPAT-PERM-01-004

- **标题**: permissions 命名差异——GitCode repository 权限项正常生效   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | ==completed_success | COVERED |  |
| 2 | run_logs | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 3 | run_logs | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 4 | workflow_parse | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
