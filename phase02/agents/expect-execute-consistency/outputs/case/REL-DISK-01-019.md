# REL-DISK-01-019
- **标题**: Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
small runner 写入 51GB 应失败，日志含 "No space left on device"。

## 做了什么
fallocate -l 51G 或 dd 写入 51GB；后续 check failure step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 超磁盘空间写入失败导致 job failure |
| 2 | run_logs | positive | contains "No space left on device" | COVERED | dd/fallocate 失败时系统报磁盘满，日志真实可观测 |
