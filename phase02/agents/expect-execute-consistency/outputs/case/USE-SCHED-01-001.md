# USE-SCHED-01-001  - **标题**: schedule 不触发时的可观测提示（判定方式：llm_assisted）   - **维度**: usability   - **评级**: 断言一致

## 想测什么

schedule 未触发时平台不应完全静默；应展示下次预计触发时间；跳过的触发应留记录并附原因

## 做了什么

- 1. 配置 schedule workflow 并制造不触发条件（如 cron 作用于非默认分支）
- 2. 等待一个触发周期后检查 workflow 列表、运行列表与详情页
- 3. 确认是否展示下次预计触发时间、跳过记录及原因

- - [负向] schedule 未触发时平台不应完全静默
- - [非功能] workflow 列表应显示下次预计触发时间字段
- - [非功能] 跳过的触发应有原因记录（非默认分支、间隔过短、cron 非法、平台故障）

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | ui | negative | eval=llm_assisted | LLM_DEPENDENT | negative+llm_assisted: schedule静默行为UI可观测性需LLM评估 |
| 2 | ui | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: UI提示字段与跳过记录需LLM评估 |
