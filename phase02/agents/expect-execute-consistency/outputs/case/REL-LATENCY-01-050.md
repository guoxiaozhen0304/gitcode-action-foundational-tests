# REL-LATENCY-01-050
- **标题**: 调度延迟基准——queued→running P50/P95 等待时间
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
空闲 runner 下连续 dispatch 30 次单 job workflow，记录 queued→running 延迟，验证 P95≤60s、不应 runner 空闲但 job 死等 >10min。
## 做了什么
YAML 定义 sleep 5 单 job，harness 连续 dispatch 30 次，采样 P50/P95。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | p95_latency_seconds | nonfunctional | le 60 | COVERED | YAML reset 30 次 dispatch + sleep 5，harness 计算 P95 分位数 |
| 2 | p50_latency_seconds | nonfunctional | le 30 | COVERED | YAML assert P50≤30s，提供参考基准 |
| 3 | no_dead_wait | negative | 不应 runner 空闲但 job 死等 >10min | MISSING | 文本有负向断言"不应出现 runner 空闲但 job 死等>10min"，YAML 无对应 assertion |
