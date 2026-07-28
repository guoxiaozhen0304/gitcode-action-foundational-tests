# COMPAT-PR-01-007
- **标题**: pull_request 不支持的 activity type（labeled）不应静默退化
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 对不合法的 `pull_request.types`（如 `labeled`）在解析阶段明确报错，而非静默忽略退化为全量触发。
## 做了什么
提交含 `pull_request.types: [labeled]` 的工作流，观察保存/解析响应；若被接受，对 PR 执行非 labeled 活动观察是否触发。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative | llm_assisted 判断若被静默接受，非labeled活动不应触发 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | save_result | positive | llm_assisted 判断解析期应报错列出合法types | LLM_DEPENDENT | eval=llm_assisted |
