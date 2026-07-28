# REL-DISK-01-019
- **标题**: Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
small runner 上尝试写入 51GB 文件，验证 job=failure、日志含"No space left on device"、不应静默卡死。
## 做了什么
YAML 使用 fallocate -l 51G 或 dd 写入 52224 个 1M 块，预期上一步写满磁盘报错，随后 check failure step echo。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | COVERED | YAML fallocate/dd 真实磁盘写入命令超出上限，platform 日志确认 job 失败 |
| 2 | run_logs | positive | contains "No space left on device" | COVERED | YAML assert 日志含磁盘满错误（内核级日志 → GENUINE），对应文本"日志含 No space left on device" |
| 3 | not_silent_hang | negative | 不应静默卡死 | COVERED | job_status=failure + 日志含明确错误 → 非静默，对应文本负向断言 |
