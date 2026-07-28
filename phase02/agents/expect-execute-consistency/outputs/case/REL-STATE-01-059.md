# REL-STATE-01-059
- **标题**: 运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
3并行job(sleep60)完成后，run终态completed/conclusion=success，收敛≤120s，状态单调无抖动，不应超过10分钟in_progress。

## 做了什么
3个独立job各sleep 60s，harness每10s轮询状态。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_conclusion | positive | equals=success | COVERED | 文本"run终态status=completed且conclusion=success"对应 |
| 2 | run_status_after_jobs_terminal | negative | equals=in_progress | COVERED | 文本"不应超过10分钟停留in_progress(#55回归)"精确对应 |
| 3 | convergence_seconds | nonfunctional | le=120 | COVERED | 文本"收敛时延≤120秒"精确对应 |
| 4 | status_sequence_monotonic | nonfunctional | equals=true | COVERED | 文本"轮询状态序列单调，无抖动(#19回归)"精确对应 |
