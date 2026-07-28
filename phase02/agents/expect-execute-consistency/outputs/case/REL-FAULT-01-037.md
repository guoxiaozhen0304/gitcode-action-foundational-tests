# REL-FAULT-01-037
- **标题**: 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
runner→平台方向网络分区 300s，验证终态可归因（续跑 success 或明确失联 failure 含归因），不应无归因说明，记录首次判死时间点。
## 做了什么
YAML 定义 3 个 step（pre marker / long work 420s / post marker），fault_injection network_partition scope runner_to_platform duration 300s at step 2。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | outcome | positive | resumed_success_or_explicit_lost_with_attribution | COVERED | YAML echo marker + fault_injection，platform 日志确定终态归属，对应文本"续跑成功；或超过平台宣告阈值后判失联失败且归因明确" |
| 2 | failure_attribution | negative | equals missing | COVERED | YAML 负向断言 failure_attribution ≠ missing（即归因必须存在），对应文本"不应出现无任何归因说明的失败" |
| 3 | first_misjudge_or_death_threshold_seconds | nonfunctional | equals recorded | COVERED | YAML assert 首次判死时间点记录，对应文本"实测心跳判死阈值回写" |
