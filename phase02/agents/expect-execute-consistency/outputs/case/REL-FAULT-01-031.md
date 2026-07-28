# REL-FAULT-01-031
- **标题**: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补两条缺失断言：step_two_marker 日志保留（原仅查 step_one）；不应 in_progress 挂起超 5 分钟（negative）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | ✅ COVERED | kill_runner 故障注入 |
| 2 | run_logs | positive | contains step_one_marker | ✅ GENUINE | step 1 真实输出 |
| 3 | run_logs | positive | contains step_two_marker | ✅ GENUINE | step 2 真实输出 |
| 4 | run_logs | negative | contains step_four_marker | ✅ GENUINE | 中断后步骤不应执行 |
| 5 | in_progress_hang_beyond_5min_detected | negative | equals true | ✅ COVERED | harness 观测挂起时长 |
