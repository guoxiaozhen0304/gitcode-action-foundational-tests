# REL-FAULT-01-033
- **标题**: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
small runner 预填充 49.5GB 后再写入 2GB artifact，验证 job=failure、日志含"No space left on device"。
## 做了什么
YAML 使用 fallocate/dd 预填充 49.5GB（50688 个 1M 块），再用 dd 写 2GB（2048 个 1M 块），fault_injection disk_full。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | COVERED | YAML fallocate/dd 真实磁盘写入超上限，platform 日志确认失败 |
| 2 | run_logs | positive | contains "No space left on device" | COVERED | YAML assert 日志含"No space left on device"，内核级错误 → GENUINE |
