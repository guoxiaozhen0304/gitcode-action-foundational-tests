# REL-RACE-01-048
- **标题**: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
jobA运行中被手动取消→jobB(needs:jobA, if:failure())应skipped而非执行。

## 做了什么
jobA sleep 60s(留窗口手动取消)，jobB needs jobA + if:failure()。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals=canceled | COVERED | 文本"jobA状态=cancelled"精确对应(YAML用canceled拼写) |
| 2 | job_b_status | positive | equals=skipped | COVERED | 文本"jobB状态=skipped"精确对应 |
