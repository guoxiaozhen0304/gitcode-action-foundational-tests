# COMPAT-PR-01-010
- **标题**: 存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
确认 GitCode 处理合并冲突 PR 的触发策略是否与 GitHub 对齐——GitHub 在有合并冲突时不触发 pull_request 运行。
## 做了什么
向已有合并冲突的 PR 推送更新，制造 pull_request update 活动，观察是否产生 workflow 运行记录。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative | llm_assisted 判断冲突PR update不应产生运行 | LLM_DEPENDENT | eval=llm_assisted，需人工判定触发策略 |
| 2 | run_list | nonfunctional | llm_assisted 结论回写Parity Matrix | LLM_DEPENDENT | type=nonfunctional/eval=llm_assisted，文档化任务 |
