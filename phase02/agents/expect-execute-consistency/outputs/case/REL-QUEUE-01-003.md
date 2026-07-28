# REL-QUEUE-01-003
- **标题**: concurrency QUEUE 策略——超上限运行应排队等待
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
concurrency.max=2 exceed-action=QUEUE，同时触发4次，运行1-2 in_progress、3-4 queued、全部最终success、3-4不被丢弃。

## 做了什么
harness同时触发4次workflow，每次sleep 30s。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed(success) | COVERED | 文本"4个运行最终全部completed(success)"对应(每个run status=success) |
| 2 | queued_count | nonfunctional | equals=2 | COVERED | 文本"运行3-4进入queued"，YAML精确断言排队数=2 |
