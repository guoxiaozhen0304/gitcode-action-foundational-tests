# COMP-TIMEOUT-01-002
- **标题**: 超时的 job 被强制终止并标记为 failure   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals: success | COVERED | sleep 120 超 timeout-minutes:1，status 不为 success |
| 2 | run_status | positive | equals: failure | COVERED | 平台杀死超时 job，标记 failure |
| 3 | run_logs | positive | contains: starting | COVERED | step echo starting（超时前日志保留） |
