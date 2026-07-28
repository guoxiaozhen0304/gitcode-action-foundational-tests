# REL-MATRIX-01-027
- **标题**: matrix max-parallel=4——9 个组合应最多同时运行 4 个
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
3x3 matrix 配 max-parallel=4 时，峰值并发≤4，9个全部success，不应超过4个同时运行。

## 做了什么
9个实例各 sleep 10秒，观察并发数。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | max_concurrent_jobs | positive | le=4 | COVERED | 文本"峰值并发≤4"精确对应 |
| 2 | run_status | positive | equals=completed(success) | COVERED | 文本"9个jobs全部completed(success)"直接对应 |
