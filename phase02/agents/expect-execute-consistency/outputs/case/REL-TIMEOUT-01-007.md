# REL-TIMEOUT-01-007
- **标题**: job timeout 边界值——359 分钟运行应在 360 分钟边界前完成   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 timeout-minutes=360 时，运行 359 分钟（sleep 21540）的 job 应正常成功完成，不被提前终止。
## 做了什么
触发 timeout-minutes=360 的 workflow，job 执行 sleep 21540（359 分钟）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | 平台 API 查询 job 终态 |
| 2 | job_duration_minutes | nonfunctional | le "359" | COVERED | harness 测量实际运行时长 |
