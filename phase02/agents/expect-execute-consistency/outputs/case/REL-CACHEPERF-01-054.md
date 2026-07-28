# REL-CACHEPERF-01-054
- **标题**: 缓存加速比——cache 命中 vs 未命中构建耗时对比
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
install 步骤去掉 `|| true`（吞失败），改为真实计时：date 前后打点输出 INSTALL_DURATION_SECONDS；新增 must_contain 确定性锚点。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | speedup_ratio | nonfunctional | ge 2 | ✅ COVERED | harness 跨 run（命中/未命中）测量比值 |
| 2 | restore_time_seconds | nonfunctional | le 30 | ✅ COVERED | harness 计时测量 |
| 3 | run_logs | positive | must_contain INSTALL_DURATION_SECONDS= | ✅ GENUINE | 真实计时命令输出 |
