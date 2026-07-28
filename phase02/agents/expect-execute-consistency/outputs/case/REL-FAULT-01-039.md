# REL-FAULT-01-039
- **标题**: 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
queued 期间下线唯一匹配 runner，≤600s 脱离 queued，runner 恢复后新 job 正常调度。

## 做了什么
单 job（runs-on self-hosted arch=x64 group=006），fault_injection 在 queued 阶段 kill 唯一匹配 runner。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | queued_escape_seconds | nonfunctional | le 600 | LLM_DEPENDENT | 非功能延迟指标 |
| 2 | queued_stall_beyond_window_detected | negative | equals "true" | MISSING | workflow 自身不产出悬挂检测标记；需 harness 侧监控 |
| 3 | post_recovery_new_job_scheduled | positive | equals "true" | MISSING | 需 harness 重新触发新 job 并验证调度成功 |
