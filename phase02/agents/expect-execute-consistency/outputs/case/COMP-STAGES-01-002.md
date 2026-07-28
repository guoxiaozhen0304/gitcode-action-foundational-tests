# COMP-STAGES-01-002
- **标题**: fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | job_status | positive | equals: skipped_for_should_skip | COVERED | fail-job exit 1 导致 should-skip 被跳过 |
| 2 | stage_execution | negative | equals: deploy_stage_executed | COVERED | 前一 stage fail_fast 失败，deploy stage 不应执行 |
