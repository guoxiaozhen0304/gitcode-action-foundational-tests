# REL-NEEDS-01-027
- **标题**: needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 needs 依赖 matrix job 的部分失败路径：jobB 3 个实例中 1 个失败，jobA 无 if 条件时应被 skipped 而非执行。
## 做了什么
提交 workflow：jobB 为 3 实例 matrix（fail-fast=false, version=2 实例 exit 1），jobA needs jobB 不附加 if 条件。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status | positive | equals "failure" | COVERED | 平台 API 查询 matrix job 聚合状态（部分失败→failure） |
| 2 | job_a_status | positive | equals "skipped" | COVERED | 平台 API 查询下游 job 状态 |
| 3 | succeeded_instances_count | positive | equals "2" | COVERED | harness 统计 matrix 中成功的实例数 |
| 4 | job_a_status | negative | equals "success" | COVERED | 验证 jobA 不应在部分失败时被执行 |
