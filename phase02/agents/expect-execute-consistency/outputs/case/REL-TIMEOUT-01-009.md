# REL-TIMEOUT-01-009
- **标题**: 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 timeout-minutes=1 时，运行 2 分钟（sleep 120）的 job 应在 60±10 秒时被终止，状态为 failure。
## 做了什么
触发 timeout-minutes=1 的 workflow，step 执行 sleep 120。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 平台 API 查询 job 终态 |
| 2 | job_duration_seconds | nonfunctional | le "70" | COVERED | harness 测量实际运行时长，≤70 秒（60+10） |
