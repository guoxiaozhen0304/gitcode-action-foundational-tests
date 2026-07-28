# COMPAT-PR-01-005
- **标题**: PR paths 过滤不工作时的兼容性差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode `pull_request.paths` 过滤功能是否与 GitHub 一致——修改匹配路径的 PR 应触发 workflow，不匹配则不触发。
## 做了什么
提交含 `pull_request.paths: ['api/**']` 的工作流，创建修改 `api/` 路径的 PR，观察触发情况。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | llm_assisted 判断PR修改匹配路径后不应无触发 | LLM_DEPENDENT | eval=llm_assisted，需人工判定是否触发 |
| 2 | run_status | positive | llm_assisted 判断修复后应触发workflow | LLM_DEPENDENT | eval=llm_assisted，需人工判定运行状态 |
