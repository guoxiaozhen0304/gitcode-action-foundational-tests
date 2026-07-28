# COMP-STAGES-01-004
- **标题**: map 形式 stages 按定义顺序串行执行（回归保护）   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 |
| 2 | run_logs | positive | must_contain: STAGE_ONE_DONE | COVERED | step echo STAGE_ONE_DONE |
| 3 | run_logs | positive | must_contain: STAGE_TWO_DONE | COVERED | step echo STAGE_TWO_DONE |
| 4 | run_logs | positive | must_contain: STAGE_ORDER_OK | COVERED | step 条件验证后 echo STAGE_ORDER_OK |
| 5 | run_logs | negative | must_not_contain: STAGE_ORDER_BROKEN | COVERED | step 仅失败路径写此值 |
