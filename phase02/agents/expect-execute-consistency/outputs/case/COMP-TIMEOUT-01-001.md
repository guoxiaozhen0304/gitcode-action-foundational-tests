# COMP-TIMEOUT-01-001
- **标题**: 未声明 timeout-minutes 的 job 在 360 分钟内正常完成
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
步骤由裸 echo "done"（STATUS_GUARANTEED）改为真实计时工作步骤（date 打点 + sleep + 输出 STEP_DURATION_SECONDS）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | 真实命令序列（date/sleep/算术） |
| 2 | run_duration | nonfunctional | less_than_minutes 360 | ✅ COVERED | harness 计时测量 |
