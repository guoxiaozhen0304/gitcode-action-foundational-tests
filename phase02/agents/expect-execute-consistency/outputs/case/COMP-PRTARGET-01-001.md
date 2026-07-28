# COMP-PRTARGET-01-001
- **标题**: pull_request_target 默认使用 base 分支 workflow 版本   - **维度**: 完备性   - **评级**: 部分不符
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains: BASE_VERSION_MARKER | COVERED | step 直接 echo BASE_VERSION_MARKER |
| 2 | run_logs | negative | must_not_contain: FORK_VERSION_MARKER | VACUOUS | R4: step 从不写 FORK_VERSION_MARKER，断言真空成立 |
