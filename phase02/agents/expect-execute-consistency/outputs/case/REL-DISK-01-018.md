# REL-DISK-01-018
- **标题**: Runner 磁盘边界——small runner 写入 49 GB 应成功
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
small runner 上写入 49GB 文件，验证 job=success，不应在 49GB 时报磁盘满。
## 做了什么
YAML 使用 fallocate -l 49G 或 dd 写入 50176 个 1M 块，随后 df -h 验证磁盘空间 + test -f 验证文件存在。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals success | COVERED | YAML fallocate/dd 真实磁盘写入命令 + df/test -f 验证，platform 日志确认成功 |
| 2 | disk_full_at_49GB | negative | 不应在 49 GB 时报磁盘满 | COVERED | job_status=success 隐含磁盘未满，对应文本负向断言 |
