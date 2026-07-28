# REL-LATENCY-01-050
- **标题**: 调度延迟基准——queued→running P50/P95 等待时间
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
空闲 runner 下 N=30 次 dispatch，P95≤60s，P50≤30s，无死等>10min。

## 做了什么
单 job sleep 5s；harness 管理 30 次 dispatch 并收集延迟数据。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | p95_latency_seconds | nonfunctional | le 60 | LLM_DEPENDENT | 非功能分位数指标，需 harness 从 30 次采样中计算 |
| 2 | p50_latency_seconds | nonfunctional | le 30 | LLM_DEPENDENT | 同上 |
| 3 | queued_stall_beyond_10min_detected | negative | equals "true" | MISSING | workflow 自身不产出悬挂检测标记；需 harness 侧监控 |
