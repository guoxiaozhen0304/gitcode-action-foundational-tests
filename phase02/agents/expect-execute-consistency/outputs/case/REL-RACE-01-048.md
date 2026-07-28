# REL-RACE-01-048
- **标题**: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证取消与 needs 条件之间的竞态处理：job A 运行中被手动取消（status=cancelled），job B（needs: job_a, if: failure()）应被 skipped 而非执行。
## 做了什么
触发含 job_a（sleep 60，运行中被手动取消）和 job_b（needs: job_a, if: failure()）的 workflow。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals "canceled" | COVERED | 平台 API 查询 job_a 状态 |
| 2 | job_b_status | positive | equals "skipped" | COVERED | 平台 API 查询 job_b 状态，cancelled≠failure 故 skipped |
