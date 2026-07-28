# COMP-STEP-01-069
- **标题**: step 必填与核心字段 name run uses 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: run_ok | COVERED | step 条件分支 echo run_ok |
| 2 | run_status | positive | equals: success | COVERED | 平台提供 |
