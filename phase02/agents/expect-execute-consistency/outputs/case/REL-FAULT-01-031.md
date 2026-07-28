# REL-FAULT-01-031
- **标题**: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
在 job 执行到第 3 个 step 时注入 SIGKILL，验证 job=failure、step 1-2 日志完整、step 3 日志不完整/标记中断、不应 in_progress 挂起 >5min。
## 做了什么
YAML 定义 5 个 step（step1-5 各有 echo marker），fault_injection kill_runner at step 3。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals failure | COVERED | YAML 使用 echo marker 真实命令 + fault_injection kill_runner，platform 日志确认失败 |
| 2 | run_logs | positive | contains step_one_marker | COVERED | YAML assert step_one_marker 存在，证明 step 1 日志已保留 |
| 3 | run_logs | negative | contains step_four_marker | COVERED | YAML 负向断言 step_four_marker 不应存在，证明 step 3 后中断 |
| 4 | step_two_log_complete | positive | step 1-2 日志完整 | NOT_COVERED | YAML 仅检查 step_one_marker，未检查 step_two_marker，文本要求的"step 1-2 日志完整"只覆盖了 step 1 |
| 5 | no_long_hang | negative | 不应 in_progress 挂起 >5min | MISSING | 文本有负向断言"不应状态=in_progress 挂起超过 5 分钟"，YAML 无对应 assertion |
