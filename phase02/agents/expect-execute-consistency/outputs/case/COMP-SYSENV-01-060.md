# COMP-SYSENV-01-060
- **标题**: ATOMGIT 系统环境变量值正确性   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: SHA_MATCH=yes | COVERED | step 对比 ATOMGIT_SHA vs atomgit.sha |
| 2 | run_logs | positive | must_contain: REF_MATCH=yes | COVERED | step 对比 ATOMGIT_REF vs atomgit.ref |
| 3 | run_logs | positive | must_contain: EVENT_MATCH=yes | COVERED | step 对比 ATOMGIT_EVENT_NAME vs atomgit.event_name |
