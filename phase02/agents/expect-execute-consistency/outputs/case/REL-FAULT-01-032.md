# REL-FAULT-01-032
- **标题**: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补缺失的负向断言：不应无限挂起超 120 秒（negative hang_beyond_120s_detected）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals failure | ✅ COVERED | 网络分区故障注入 |
| 2 | run_logs | positive | contains network | ✅ COVERED | 网络错误日志 |
| 3 | hang_beyond_120s_detected | negative | equals true | ✅ COVERED | harness 观测挂起时长 |
