# USE-UNKN-01-001  - **标题**: 未知字段如 run-name 不应被静默忽略而应给出警告或错误   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

系统在校验阶段给出警告或错误，指明字段不支持

## 做了什么

- 1. 在 workflow 中使用 GitHub 特有的 run-name 字段

- - [负向] 不应静默忽略未知字段
- - [非功能] 报错中是否包含字段名、文件路径、不支持字样

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 未知字段报错文案质量需LLM评估; YAML含run-name→真实平台校验 |
