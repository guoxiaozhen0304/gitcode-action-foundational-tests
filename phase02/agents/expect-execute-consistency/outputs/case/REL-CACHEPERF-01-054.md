# REL-CACHEPERF-01-054
- **标题**: 缓存加速比——cache 命中 vs 未命中构建耗时对比
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
cache 命中后 npm ci ≤ 0.5× 冷安装耗时，restore≤30s。

## 做了什么
单 workflow 含 cache restore + npm ci 计时输出 INSTALL_DURATION_SECONDS。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | speedup_ratio | nonfunctional | ge 2 | LLM_DEPENDENT | 跨 run 对比指标，需 harness 统计命中/未命中两轮耗时比，workflow 仅输出计时标记 |
| 2 | restore_time_seconds | nonfunctional | le 30 | LLM_DEPENDENT | 非功能性能指标，由 harness 测量 |
| 3 | run_logs | positive | must_contain "INSTALL_DURATION_SECONDS=" | COVERED | install deps step 真实 echo 耗时标记 |
