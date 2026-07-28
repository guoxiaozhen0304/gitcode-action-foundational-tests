# COMPAT-PR-01-004
- **标题**: PR types 含 merge 时不触发与 GitHub 行为差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 处理 `pull_request.types` 含 `merge` 时的触发行为，确认是否与 GitHub 一致（GitHub 合并 PR 触发 pull_request merge 独立 Job，GitCode 目前仅产生 PUSH 运行）。
## 做了什么
提交含 `pull_request.types: [open, merge]` 的工作流，合并 PR 后观察运行记录，比对差异。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断合并后不虚仅有PUSH运行 | LLM_DEPENDENT | eval=llm_assisted，需人工判定运行事件类型 |
| 2 | run_status | positive | llm_assisted 判断修复后应触发PR运行 | LLM_DEPENDENT | eval=llm_assisted，需人工判定运行是否对应PR事件 |
