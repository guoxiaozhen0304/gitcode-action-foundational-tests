# COMP-STAGES-01-001
- **标题**: stages 阶段间串行、阶段内 job 并行执行   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | 平台提供 |
| 2 | run_logs | positive | must_contain: BUILD_A_START= | COVERED | step echo BUILD_A_START=\$(date +%s) |
| 3 | run_logs | positive | must_contain: BUILD_B_START= | COVERED | step echo BUILD_B_START=\$(date +%s) |
| 4 | run_logs | positive | must_contain: TEST_START= | COVERED | step echo TEST_START=\$(date +%s) |
| 5 | stage_order | positive | equals: serial_across_stages | COVERED | 日志时间戳供 harness 验证 |
| 6 | job_parallelism | positive | equals: parallel_within_stage | COVERED | 日志时间戳供 harness 验证 |
