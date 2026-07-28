# COMPAT-PERM-01-006

- **标题**: job 级 permissions 字段的支持度与降级方式（权限不得宽于声明）   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 2 | save_result | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 3 | save_result | nonfunctional | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
