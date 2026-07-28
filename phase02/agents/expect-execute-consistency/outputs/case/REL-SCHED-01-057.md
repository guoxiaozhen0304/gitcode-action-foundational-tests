# REL-SCHED-01-057
- **标题**: 资源调度状态一致性——空闲 runner 存在时 job 不应死等   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证空闲 runner 存在时 job 的调度延迟有界：10 次顺序触发，每次 queued→running ≤60s，平均 ≤30s。
## 做了什么
连续触发 10 次单 job workflow（每 job sleep 30s），每次等待 runner 空闲后再触发下一次。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | max_queued_to_running_seconds | nonfunctional | le "60" | COVERED | harness 测量每次的最大 queued→running 时延 |
| 2 | avg_queued_to_running_seconds | nonfunctional | le "30" | COVERED | harness 计算 10 次的平均调度时延 |
