# COMP-PUSH-01-001
- **标题**: 匹配 branches 的 push 正确触发 workflow   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 |
| 2 | run_event | positive | equals: push | COVERED | 平台提供 |
| 3 | run_logs | positive | must_contain: TRIGGERED_ON_MAIN_OK | COVERED | step 条件分支 echo |
