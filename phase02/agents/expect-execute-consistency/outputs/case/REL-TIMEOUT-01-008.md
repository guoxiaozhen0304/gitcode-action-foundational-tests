# REL-TIMEOUT-01-008
- **标题**: job timeout 越界触发——361 分钟应在 360 分钟被强制终止   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 timeout-minutes=360 时，运行 361 分钟（sleep 21660）的 job 应在 ~360 分钟时被强制终止，状态为 failure，日志含 timeout 信息。
## 做了什么
触发 timeout-minutes=360 的 workflow，job 执行 sleep 21660（361 分钟）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 平台 API 查询 job 终态 |
| 2 | run_logs | positive | contains "timeout" | COVERED | harness 解析日志查找 timeout/超时关键字 |
