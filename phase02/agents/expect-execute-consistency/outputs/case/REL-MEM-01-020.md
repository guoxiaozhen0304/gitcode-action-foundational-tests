# REL-MEM-01-020
- **标题**: Runner 内存边界——small runner 分配 7.5 GB 应成功   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 small runner 在分配 7.5 GB 内存时应成功完成，不应在 7 GB 时 OOM。
## 做了什么
触发 runs-on small 的 job，通过 python3 分配 7680*1024*1024 bytearray（约 7.5 GB）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | 平台 API 查询 job 终态；若 OOM 则状态为 failure |
