# COMPAT-PR-01-008
- **标题**: pull_request 不支持的 activity type（ready_for_review）不应静默不触发
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 对不合法的 `pull_request.types`（如 `ready_for_review`）在解析阶段明确报错，而非静默接受后永不触发且无提示。
## 做了什么
提交含 `pull_request.types: [ready_for_review]` 的工作流，观察保存/解析响应；若被接受，将 draft PR 转正式观察触发情况。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative | llm_assisted 判断静默接受后不应永不触发无提示 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | save_result | positive | llm_assisted 判断解析期应报错列出合法types | LLM_DEPENDENT | eval=llm_assisted |
