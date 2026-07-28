# REL-FAULT-01-039
- **标题**: 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
job 处于 queued 时下线唯一匹配 runner，验证 ≤600s 脱离 queued（重调度或明确失败）、不无限挂起 >10min、runner 恢复后新 job 调度成功。
## 做了什么
YAML 使用 runs-on [self-hosted,...]，fault_injection kill_runner phase queued target only_matching_runner method stop_agent_process。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | queued_escape_seconds | nonfunctional | le 600 | COVERED | YAML self-hosted runner + fault_injection，harness 观测脱离 queued 时间 ≤600s |
| 2 | queued_stall_beyond_window_detected | negative | equals true | COVERED | YAML 负向检测不应 queued 挂起 >10min，对应文本"不无限 queued 挂起" |
| 3 | post_recovery_new_job_scheduled | positive | equals true | COVERED | YAML assert runner 恢复后新 job 调度成功，对应文本"runner 重新上线后新触发 job 正常调度" |
