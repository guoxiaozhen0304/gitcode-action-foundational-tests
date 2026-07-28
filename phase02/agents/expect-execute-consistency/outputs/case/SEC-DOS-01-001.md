# SEC-DOS-01-001
- **标题**: 大 artifact / 大 cache 必须受配额与边界限制   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
超过大小上限的artifact/cache上传不应成功，job以failure结束并给出明确报错。
## 做了什么
YAML workflow创建1.1GB文件(dd)，使用upload-artifact action上传，trigger为workflow_dispatch。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | must_not_equal "success" | COVERED | 运行状态为平台可观测值 |
| 2 | job_status | positive | equals "failure" | COVERED | job状态为平台可观测值 |
