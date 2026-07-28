# REL-DISK-01-018
- **标题**: Runner 磁盘边界——small runner 写入 49 GB 应成功
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
small runner 写入 49GB 成功，剩余约 1GB。

## 做了什么
fallocate -l 49G 或 dd 写入 49GB；df -h 验证；test -f 检查文件存在。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | fallocate/dd 成功则 job success |
