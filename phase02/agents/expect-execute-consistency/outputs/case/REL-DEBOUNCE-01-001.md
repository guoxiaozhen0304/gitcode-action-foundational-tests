# REL-DEBOUNCE-01-001
- **标题**: 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
10s 内 5 次 push，run 与 sha 一一对应；无重复触发。

## 做了什么
workflow on push branches=[main]；step echo trigger_sha；由 harness 管理连续 push。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | push_sha_run_mapping | positive | equals "1:1_or_documented_debounce" | MISSING | workflow 仅 echo sha，不对账；对账逻辑完全在 harness 侧，YAML 内无验证步骤 |
| 2 | same_sha_duplicate_runs_count | positive | equals "0" | MISSING | 同上，需 harness 侧统计 |
| 3 | unexplained_run_loss_detected | negative | equals "true" | MISSING | 需 harness 侧对账判定 |
