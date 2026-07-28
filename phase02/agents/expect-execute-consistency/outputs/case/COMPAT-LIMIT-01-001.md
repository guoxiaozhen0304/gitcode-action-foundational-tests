# COMPAT-LIMIT-01-001

- **标题**: 单次推送多个 tag 的事件生成上限行为（GitHub 超过 3 个不生成事件）   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | positive | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
| 2 | run_list | negative | eval:llm_assisted | COVERED | llm_assisted (LLM→断言一致) |
