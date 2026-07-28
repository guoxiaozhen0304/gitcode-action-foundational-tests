# COMPAT-SCHEDULE-01-003
- **标题**: schedule 在非默认分支不触发与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 的 schedule workflow 是否仅在默认分支触发（与 GitHub 行为一致），非默认分支不应触发。
## 做了什么
在 develop 分支创建 schedule workflow，等待 cron 触发时间，观察运行情况。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | llm_assisted 判断非默认分支不应触发 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_status | positive | llm_assisted 判断默认分支正常触发 | LLM_DEPENDENT | eval=llm_assisted |
