# REL-STATE-01-058
- **标题**: Runner 状态机正确性——空闲/运行/离线转换与时序一致性
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
对同一runner连续触发5轮，状态序列idle→running→idle正确，转换时延有界(idle→running≤30s, running→idle≤60s)。

## 做了什么
job sleep 60s，harness观测runner状态。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | state_sequence | positive | equals=idle_running_idle | COVERED | 文本"状态序列符合idle→running→idle"精确对应 |
| 2 | idle_to_running_seconds | nonfunctional | le=30 | COVERED | 文本"idle→running≤30s"精确对应 |
| 3 | running_to_idle_seconds | nonfunctional | le=60 | COVERED | 文本"running→idle≤60s"精确对应 |
