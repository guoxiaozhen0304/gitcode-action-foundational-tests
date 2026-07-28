# COMPAT-PR-01-006
- **标题**: PR 目标分支过滤行为差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode `pull_request.branches` 目标分支过滤功能——目标为 main 的 PR 应触发，目标为 develop 的不应触发。
## 做了什么
提交含 `pull_request.branches: [main]` 的工作流，分别创建目标为 main 和 develop 的 PR，观察触发差异。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | llm_assisted 判断main分支PR应触发 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_status | negative | llm_assisted 判断非main分支PR不应触发 | LLM_DEPENDENT | eval=llm_assisted |
