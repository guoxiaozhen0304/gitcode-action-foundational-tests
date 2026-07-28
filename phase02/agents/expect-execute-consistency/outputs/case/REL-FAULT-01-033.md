# REL-FAULT-01-033
- **标题**: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
预填充 49.5GB 后再写 2GB，job=failure，日志含磁盘满错误。

## 做了什么
prefill 49.5GB + write 2GB extra；两个 dd/fallocate step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 写 2GB 超出剩余空间，job 失败 |
| 2 | run_logs | positive | contains "No space left on device" | COVERED | 系统磁盘满错误可观测 |
