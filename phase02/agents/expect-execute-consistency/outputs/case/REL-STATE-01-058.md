# REL-STATE-01-058
- **标题**: Runner 状态机正确性——空闲/运行/离线转换与时序一致性   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 Runner 状态机在 5 轮触发→运行→空闲循环中的转换正确性：状态序列符合 idle→running→idle，转换时延有界（idle→running ≤30s，running→idle ≤60s）。
## 做了什么
对同一 runner 连续执行触发→观察→等待→触发循环 5 轮，每轮 sleep 60s。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | state_sequence | positive | equals "idle_running_idle" | COVERED | harness 轮询 runner 状态验证序列正确 |
| 2 | idle_to_running_seconds | nonfunctional | le "30" | COVERED | harness 测量 idle→running 转换时延 |
| 3 | running_to_idle_seconds | nonfunctional | le "60" | COVERED | harness 测量 running→idle 转换时延 |
