# REL-NEEDS-01-026
- **标题**: needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
jobB(martix 3实例全success)→jobA(needs:jobB)正常初始化success，needs.jobB.result=success，不应初始化失败(#101回归)。

## 做了什么
jobB 3实例matrix全echo标记(无失败)，jobA needs jobB并输出needs result。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status | positive | equals=success | COVERED | 文本"jobB全部matrix实例状态=success"对应 |
| 2 | job_a_status | positive | equals=success | COVERED | 文本"jobA状态=success"精确对应 |
| 3 | job_a_status | negative | equals=skipped | COVERED | 文本"jobA不应初始化失败或状态=skipped"精确对应(#101回归) |
| 4 | downstream_start_delay_seconds | nonfunctional | le=120 | COVERED | 文本"聚合判定延迟≤120秒"精确对应 |
