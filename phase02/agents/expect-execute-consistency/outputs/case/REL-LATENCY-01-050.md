# REL-LATENCY-01-050
- **标题**: 调度延迟基准——queued→running P50/P95 等待时间
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补缺失的负向断言：不应 runner 空闲但 job 死等超 10 分钟（negative queued_stall_beyond_10min_detected）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | p95_latency_seconds | nonfunctional | le 60 | ✅ COVERED | harness 30 次采样 P95 |
| 2 | p50_latency_seconds | nonfunctional | le 30 | ✅ COVERED | harness 采样 P50 |
| 3 | queued_stall_beyond_10min_detected | negative | equals true | ✅ COVERED | harness 观测死等 |
