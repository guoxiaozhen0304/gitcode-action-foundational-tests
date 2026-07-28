# REL-FAIR-01-044
- **标题**: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补规格中缺失的负向断言：不应出现 X 全部完成后 Y 才开始（negative serial_execution_detected equals true，语义=不应检测到串行执行）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | startup_time_diff_seconds | nonfunctional | le 60 | ✅ COVERED | harness 测量两 workflow 首 job 启动时延差 |
| 2 | serial_execution_detected | negative | equals true | ✅ COVERED | 负向：不得串行执行 |
