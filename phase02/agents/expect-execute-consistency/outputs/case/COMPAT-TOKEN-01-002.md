# COMPAT-TOKEN-01-002
- **标题**: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 不将 GITHUB_TOKEN 静默映射为 ATOMGIT_TOKEN——GITHUB_TOKEN 应为空或未定义，引用时应返回 401/403。
## 做了什么
通过 `${{ secrets.GITHUB_TOKEN }}` 引用令牌发起 API 调用，检查 HTTP 状态码。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断api_status应为401/403 | LLM_DEPENDENT | eval=llm_assisted，需人工确认状态码不是200 |
| 2 | error_message | nonfunctional | llm_assisted 判断报错应提示使用ATOMGIT_TOKEN | LLM_DEPENDENT | type=nonfunctional，文档化建议任务 |
