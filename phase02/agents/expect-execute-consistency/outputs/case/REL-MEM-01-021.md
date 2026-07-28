# REL-MEM-01-021
- **标题**: Runner 内存越界——small runner 分配 9 GB 应被 OOM kill   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 small runner 在分配 9 GB 内存超出上限时应被 OOM kill，日志含 Killed 信息。
## 做了什么
触发 runs-on small 的 job，通过 python3 分配 9216*1024*1024 bytearray（约 9 GB）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | 平台 API 查询 job 终态为 failure |
| 2 | run_logs | positive | contains "Killed" | COVERED | harness 解析日志查找 OOM/Killed 关键字 |
