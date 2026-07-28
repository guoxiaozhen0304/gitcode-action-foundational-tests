# REL-FAULT-01-035
- **标题**: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
在 download-artifact 期间注入服务 503，验证 step=failure、日志含 503/service unavailable、job=failure。
## 做了什么
YAML 使用 download-artifact action（下载不存在的 artifact），fault_injection 对 artifact_download 服务注入 503。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals failure | COVERED | YAML download-artifact action + fault_injection，platform/action 日志确认 step 失败 |
| 2 | run_logs | positive | contains 503 | COVERED | YAML assert 日志含 503，action 层面错误信息 → GENUINE |
| 3 | job_status | positive | equals failure | COVERED | YAML assert job_status=failure，对应文本"job 状态=failure" |
