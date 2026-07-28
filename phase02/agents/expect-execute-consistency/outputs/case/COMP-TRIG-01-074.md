# COMP-TRIG-01-074
- **标题**: workflow_dispatch 事件关键字段与 inputs 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: ENV= | COVERED | step echo ENV=\${{ inputs.environment }} |
| 2 | run_logs | positive | must_contain: VER= | COVERED | step echo VER=\${{ inputs.version }} |
| 3 | run_logs | positive | must_contain: dispatch_ok | COVERED | step echo dispatch_ok |
