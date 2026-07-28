# REL-NEEDS-01-026
- **标题**: needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 needs 依赖 matrix job 的成功路径：jobB 的 3 个 matrix 实例全部 success 后，jobA 应正常初始化执行（#101 回归点）。
## 做了什么
提交 workflow：jobB 为 3 实例 matrix（全部设计为成功），jobA 通过 needs 依赖 jobB，jobA 内输出 needs.jobB.result。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status | positive | equals "success" | COVERED | 平台 API 查询 matrix job 聚合状态 |
| 2 | job_a_status | positive | equals "success" | COVERED | 平台 API 查询下游 job 状态 |
| 3 | job_a_status | negative | equals "skipped" | COVERED | 验证 jobA 未因 #101 bug 被错误 skip |
| 4 | downstream_start_delay_seconds | nonfunctional | le "120" | COVERED | harness 测量聚合判定延迟 |
