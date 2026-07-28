# REL-NEEDS-01-025
- **标题**: needs 失败传播——上游 job 失败时下游 job 应被 skip   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 needs 依赖关系中上游 job 失败时，下游 job 应被 skipped 而不会执行。
## 做了什么
触发含 job_a（exit 1 失败）和 job_b（needs: job_a）的 workflow。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals "failure" | COVERED | 平台 API 查询 upstream job 状态 |
| 2 | job_b_status | positive | equals "skipped" | COVERED | 平台 API 查询 downstream job 状态为 skipped |
