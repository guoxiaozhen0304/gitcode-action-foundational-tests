# REL-NEEDS-01-025
- **标题**: needs 失败传播——上游 job 失败时下游 job 应被 skip
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
job_a失败→job_b(needs:job_a)应被skipped，不应执行。

## 做了什么
job_a执行exit 1，job_b needs job_a。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals=failure | COVERED | 文本"job_a状态=failure"精确对应 |
| 2 | job_b_status | positive | equals=skipped | COVERED | 文本"job_b状态=skipped"精确对应 |
