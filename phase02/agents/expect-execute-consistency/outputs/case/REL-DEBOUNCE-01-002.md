# REL-DEBOUNCE-01-002
- **标题**: 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
10s 内 10 个 tag push，run 对账一致，无重复触发。

## 做了什么
workflow on push tags=["v*"]；step echo trigger_ref；由 harness 管理批量 tag push。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | tag_event_run_reconciliation | positive | equals "10/10_or_documented_debounce" | MISSING | workflow 仅 echo ref，不对账；对账逻辑在 harness 侧 |
| 2 | same_tag_duplicate_runs_count | positive | equals "0" | MISSING | 需 harness 侧统计 |
| 3 | unexplained_run_loss_detected | negative | equals "true" | MISSING | 需 harness 侧对账判定 |
