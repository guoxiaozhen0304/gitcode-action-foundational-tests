# COMP-UNKNOWN-01-004
- **标题**: select 与 selected_by_default 声明时的实际行为记录   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
记录 `select: selected_by_default` 在 stage/job 两级的实际处理行为（校验报错/静默忽略/生效）。
## 做了什么
workflow_dispatch 触发，stages 中声明 select: selected_by_default，job 中 echo `SELECT_JOB_RAN`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | select_handling | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9：llm_assisted 按 断言一致 处理 |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9：llm_assisted 按 断言一致 处理 |
