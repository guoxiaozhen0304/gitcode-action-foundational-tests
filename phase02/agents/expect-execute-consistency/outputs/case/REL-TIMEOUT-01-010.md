# REL-TIMEOUT-01-010
- **标题**: 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证未声明 timeout-minutes 时使用默认超时 360 分钟：运行 361 分钟（sleep 21660）的 job 应被强制终止，状态为 failure，日志含 timeout 信息。
## 做了什么
触发未声明 timeout-minutes 的 workflow，job 执行 sleep 21660（361 分钟）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 平台 API 查询 job 终态 |
| 2 | run_logs | positive | contains "timeout" | COVERED | harness 解析日志查找 timeout 关键字 |
