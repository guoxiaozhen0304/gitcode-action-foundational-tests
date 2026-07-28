# REL-FLOOD-01-037
- **标题**: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
步骤输出 RUN_ID/RUN_NUMBER 供重复触发对账；补两条缺失断言：不应重复触发（negative duplicate_trigger_count=0）、总时长合理（nonfunctional total_duration_seconds le 1800）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals 50 | ✅ COVERED | harness 计数 |
| 2 | api_status | positive | equals 200 | ✅ COVERED | API 正常 |
| 3 | api_status | negative | equals 500 | ✅ COVERED | 无 5xx |
| 4 | duplicate_trigger_count | negative | equals 0 | ✅ COVERED | RUN_ID 对账 |
| 5 | total_duration_seconds | nonfunctional | le 1800 | ✅ COVERED | harness 计时 |
