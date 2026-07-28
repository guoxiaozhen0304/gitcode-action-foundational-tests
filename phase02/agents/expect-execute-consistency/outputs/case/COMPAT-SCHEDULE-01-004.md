# COMPAT-SCHEDULE-01-004
- **标题**: schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
确认 GitCode schedule 的自动停用/保活策略及触发延迟可观测性，与 GitHub 的 60 天无活动自动停用对比。
## 做了什么
配置最短间隔定时 workflow，观察计划时间与实际入队时间的延迟，查阅文档确认停用策略。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain SCHEDULE_PROBE_DONE | COVERED | 工作流固定输出标志字符串 |
| 2 | run_list | negative | llm_assisted 判断不应有未文档化静默停用 | LLM_DEPENDENT | eval=llm_assisted，长期观察任务 |
| 3 | run_list | nonfunctional | llm_assisted 触发延迟可观测结论文档化 | LLM_DEPENDENT | type=nonfunctional，文档化+复验TC-563 |
