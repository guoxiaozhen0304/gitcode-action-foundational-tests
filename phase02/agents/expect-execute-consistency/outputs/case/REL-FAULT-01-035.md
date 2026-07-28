# REL-FAULT-01-035
- **标题**: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
download-artifact 期间注入 503，step=failure，日志含 "503"，job=failure。

## 做了什么
download-artifact step（尝试下载不存在的 artifact）；fault_injection 注入 503。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals "failure" | COVERED | 503 导致 download 失败 |
| 2 | run_logs | positive | contains "503" | COVERED | HTTP 503 响应码在错误日志中可观测 |
| 3 | job_status | positive | equals "failure" | COVERED | step 失败导致 job 失败 |
