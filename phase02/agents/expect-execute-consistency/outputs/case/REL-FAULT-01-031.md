# REL-FAULT-01-031
- **标题**: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
step 3 时注入 SIGKILL，job=failure，step1-2 日志完整，step 4 不应出现。

## 做了什么
5 个 step（echo marker），step 3 sleep 30s；fault_injection 在 step 3 注入 kill_runner。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "failure" | COVERED | SIGKILL 后 job 应为 failure |
| 2 | run_logs | positive | contains "step_one_marker" | COVERED | step 1 已执行，echo 输出可观测 |
| 3 | run_logs | positive | contains "step_two_marker" | COVERED | step 2 已执行，echo 输出可观测 |
| 4 | run_logs | negative | contains "step_four_marker" | COVERED | step 3 被 kill，step 4 不应执行，日志不应含 step_four_marker |
| 5 | in_progress_hang_beyond_5min_detected | negative | equals "true" | COVERED | 由 harness 观测超时悬挂 |
