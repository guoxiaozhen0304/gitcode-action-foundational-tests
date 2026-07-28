# REL-MATRIXFAIR-01-056
- **标题**: 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
20实例matrix配max-parallel=4，全部完成、最大/最小延迟比≤3、无饿死。

## 做了什么
20个实例各sleep 30s，观察排队延迟。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_jobs_count | positive | equals=20 | COVERED | 文本"20实例全部完成"精确对应 |
| 2 | queued_delay_ratio | nonfunctional | le=3 | COVERED | 文本"最大/最小queued延迟比≤3"精确对应 |
| 3 | (文本负向) 无实例被无限饿死 | — | — | MISSING | 文本"无实例被无限饿死"在YAML中无对应独立negative断言(可被全完成隐含) |
