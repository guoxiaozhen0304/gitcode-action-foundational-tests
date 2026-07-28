# SEC-WFRUN-01-001
- **标题**: 不可信运行绝不应存在隐式拉起高权限后续运行的链式路径
- **维度**: security
- **评级**: 部分不符

## 想测什么
fork PR 运行结束后无任何自动拉起的特权运行记录；文档应明示 workflow_run 不支持。

## 做了什么
workflow: null。断言指向外部 run_list 和 documentation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | must_not_contain:implicit_privileged_run_after_fork_pr | MISSING_SOURCE | 无 workflow 步骤产生 run_list 输出；完全依赖 harness 外部枚举 |
| 2 | documentation | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional 类型 + LLM 辅助判定文档内容 |
