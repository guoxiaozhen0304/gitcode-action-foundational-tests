# REL-FAULT-01-032
- **标题**: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
upload 期间网络分区 30s，step=failure，日志含 network 错误，不挂起超 120s。

## 做了什么
生成 10MB artifact，upload；fault_injection 在 step 2 注入 30s 网络分区。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals "failure" | COVERED | 网络分区导致 upload 失败 |
| 2 | run_logs | positive | contains "network" | COVERED | 网络错误日志可观测 |
| 3 | hang_beyond_120s_detected | negative | equals "true" | COVERED | harness 观测超时悬挂 |
