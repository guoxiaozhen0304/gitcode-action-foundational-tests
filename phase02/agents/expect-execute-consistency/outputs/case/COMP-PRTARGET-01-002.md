# COMP-PRTARGET-01-002
- **标题**: 显式 checkout head.sha 后执行不可信代码的风险可控   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 run_status |
| 2 | run_logs | positive | contains: BASE_VERSION_MARKER | COVERED | step echo BASE_VERSION_MARKER |
| 3 | run_logs | positive | contains: HEAD_SHA_CHECKOUT_OK | COVERED | if 分支 echo HEAD_SHA_CHECKOUT_OK |
