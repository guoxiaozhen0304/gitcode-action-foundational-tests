# REL-NEEDS-01-027
- **标题**: needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
jobB(3实例中1失败, fail-fast=false)→jobA(needs:jobB)应skipped，不应执行，其余2实例正常成功不被取消。

## 做了什么
jobB version=2故意exit 1，jobA needs jobB无if条件。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status | positive | equals=failure | COVERED | 文本"jobB聚合状态=failure"对应 |
| 2 | job_a_status | positive | equals=skipped | COVERED | 文本"jobA状态=skipped"精确对应 |
| 3 | succeeded_instances_count | positive | equals=2 | COVERED | 文本"成功实例数=2"精确对应 |
| 4 | job_a_status | negative | equals=success | COVERED | 文本"jobA不应被执行(状态≠success)"精确对应 |
