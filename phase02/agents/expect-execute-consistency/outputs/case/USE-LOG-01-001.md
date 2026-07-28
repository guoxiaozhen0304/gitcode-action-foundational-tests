# USE-LOG-01-001  - **标题**: 多 step 日志按时间线组织且边界清晰   - **维度**: usability   - **评级**: 断言一致

## 想测什么

step 按定义顺序排列，含时间戳前缀，长输出可折叠

## 做了什么

- 1. 触发一个含 5 个以上 steps 的 workflow
- 2. 在日志面板查看组织方式

- - [正向] 日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs 中检索到
- - [非功能] 用户能在 3 秒内定位到失败 step

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=`step one prepare` | COVERED | run_logs+contains: 'step one prepare'是步骤名→平台Runner日志头输出→GENUINE |
| 2 | step_order | positive | equals=`step one prepare,step two build,step three test,step four package,step five summary` | COVERED | step_order: 步骤顺序验证→平台可观察 |
| 3 | ui_layout | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: UI布局体验需LLM评估 |
