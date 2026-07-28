# REL-SCHED-01-057
- **标题**: 资源调度状态一致性——空闲 runner 存在时 job 不应死等
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
空闲runner时10次全部queued→running≤60s、平均≤30s、不应死等>5min。

## 做了什么
harness连续触发10次单job workflow，每次等完成再触发。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | max_queued_to_running_seconds | nonfunctional | le=60 | COVERED | 文本"10次全部≤60s"精确对应 |
| 2 | avg_queued_to_running_seconds | nonfunctional | le=30 | COVERED | 文本"平均≤30s"精确对应 |
| 3 | (文本负向) 不应死等>5min | — | — | MISSING | 文本"不应出现runner空闲但job死等>5min"在YAML中无独立negative断言 |
