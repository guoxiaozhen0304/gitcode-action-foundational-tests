# REL-CONTINUE-01-030
- **标题**: continue-on-error=true——job 失败后 workflow 不应终止
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
job_a(continue-on-error) exit 1 后 job_b 正常执行，workflow=success。

## 做了什么
job_a: continue-on-error=true, exit 1；job_b: echo "job_b executed"（无 needs 依赖）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status | positive | equals "failure" | COVERED | exit 1 导致 job 失败，状态可观测 |
| 2 | job_b_status | positive | equals "success" | COVERED | continue-on-error 允许后续 job 继续 |
| 3 | workflow_status | positive | equals "success" | COVERED | continue-on-error 后整体 workflow 应 success |
