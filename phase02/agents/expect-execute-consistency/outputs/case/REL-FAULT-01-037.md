# REL-FAULT-01-037
- **标题**: 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
300s 分区后行为确定：续跑 success 或明确失联 failure+归因。

## 做了什么
3 step job（pre_marker→sleep 420s→post_marker）；fault_injection 300s 分区在 step 2。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | outcome | positive | equals "resumed_success_or_explicit_lost_with_attribution" | COVERED | 二选一可归因行为，平台终态可观测 |
| 2 | failure_attribution | negative | equals "missing" | COVERED | 若失败则必须有归因；若续跑成功则该断言 NAT/VACUOUS |
| 3 | first_misjudge_or_death_threshold_seconds | nonfunctional | equals "recorded" | LLM_DEPENDENT | 观测记录型指标 |
