# REL-PRESSURE-01-055
- **标题**: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
10s内触发20次workflow，completed=20、running峰值≤5、总耗时≤15min、不应静默消失。

## 做了什么
concurrency max=5 queue，harness在10s内并发触发20次。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count | positive | equals=20 | COVERED | 文本"completed=20"精确对应 |
| 2 | max_running_count | nonfunctional | le=5 | COVERED | 文本"running峰值≤5"精确对应 |
| 3 | total_duration_seconds | nonfunctional | le=900 | COVERED | 文本"总耗时≤15min"(900s)精确对应 |
| 4 | (文本负向) 不应出现运行静默消失 | — | — | MISSING | 文本"不应出现运行静默消失"在YAML中无对应独立negative断言 |
