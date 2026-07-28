# REL-STATE-01-059
- **标题**: 运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 run 状态收敛：所有 job 进入终态后 ≤120 秒 run.status 收敛为 completed，conclusion=success，状态序列单调（QUEUED→RUNNING→COMPLETED），无 RUNNING↔COMPLETED 抖动（#55/#19 回归点）。
## 做了什么
触发 3 个并行 job（各 sleep 60s），自触发起每 10 秒轮询 run/job 状态，持续 10 分钟。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_conclusion | positive | equals "success" | COVERED | 平台 API 查询 run conclusion |
| 2 | run_status_after_jobs_terminal | negative | equals "in_progress" | COVERED | harness 检测 job 全终态后 run 仍为 in_progress（#55 回归点） |
| 3 | convergence_seconds | nonfunctional | le "120" | COVERED | harness 测量收敛时延 |
| 4 | status_sequence_monotonic | nonfunctional | equals "true" | COVERED | harness 验证轮询状态序列单调无抖动（#19 回归点） |
