# COMP-STATUS-01-002
- **标题**: 失败 step 的日志完整保留且可查看   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: failure | COVERED | step exit 1 |
| 2 | run_logs | positive | contains: BEFORE_FAILURE_MARKER | COVERED | step echo BEFORE_FAILURE_MARKER |
| 3 | run_logs | positive | contains: ERROR_MARKER | COVERED | step echo ERROR_MARKER 后 exit 1 |
