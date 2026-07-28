# USE-UNKN-01-002  - **标题**: 未知字段报错若识别为 GitHub 特有应追加迁移提示   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

报错除指出字段不支持外，还提示该字段为 GitHub Actions 特有

## 做了什么

- 1. 在 workflow 中使用 GitHub 特有的 jobs.<id>.container 字段

- - [非功能] 报错中是否出现 GitHub Actions 特有等迁移提示

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 未知字段报错+迁移提示质量需LLM评估 |
