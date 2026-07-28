# COMPAT-PR-01-010
- **标题**: 存在合并冲突的 PR 的触发行为对齐确认
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
确定合并冲突PR的触发策略——应与GitHub对齐（不触发）或差异被文档化。

## 做了什么
workflow 配置 `pull_request.types: [open, update]`，step输出 `echo "CONFLICT_PR_JOB_RAN"`；对该冲突PR推送update后观察是否产生运行。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative llm | "冲突PR的update不应产生运行记录" | COVERED | echo "CONFLICT_PR_JOB_RAN"为GENUINE(R1)；若run_list中无此输出即证明未触发 |
| 2 | run_list | nonfunctional llm | "触发策略结论回写Parity Matrix" | LLM_DEPENDENT | R5: nonfunctional + llm → LLM_DEPENDENT；结论需人工/LLM回写文档 |
