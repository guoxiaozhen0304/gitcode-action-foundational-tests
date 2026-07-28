# COMP-STEP-01-070
- **标题**: step 可选字段 id env if with 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: OUT=hello | COVERED | step echo OUT=\${{ steps.mystep.outputs.result }} |
| 2 | run_logs | positive | must_contain: STEP_VAR=step_value | COVERED | step echo STEP_VAR=\$STEP_VAR |
