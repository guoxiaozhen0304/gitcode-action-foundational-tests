# REL-CANCELREL-01-061
- **标题**: 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补规格中缺失的负向断言：queued 阶段取消后不应错标 success/failure（两条 negative cancel_queued_status）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cancel_queued_status | positive | equals canceled | ✅ COVERED | harness 在 queued 阶段取消观测 |
| 2 | cancel_queued_status | negative | equals success | ✅ COVERED | 负向：不得错标 success |
| 3 | cancel_queued_status | negative | equals failure | ✅ COVERED | 负向：不得错标 failure |
| 4 | cancel_running_status | positive | equals canceled | ✅ COVERED | running 阶段取消观测 |
| 5 | cancel_post_main_status | positive | equals success | ✅ COVERED | post 阶段取消观测 |
| 6 | cancel_stabilization_seconds | nonfunctional | le 60 | ✅ COVERED | harness 计时测量 |
