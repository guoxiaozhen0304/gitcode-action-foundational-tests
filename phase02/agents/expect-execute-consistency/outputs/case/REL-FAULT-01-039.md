# REL-FAULT-01-039
- **标题**: 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**排队期 runner 下线后 job 应重调度或有界失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-082
通过标准：
1. job ≤600s 内脱离 queued
2. 不应 queued >10min
3. runner 恢复后新 job 调度成功

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | probe step | `echo "rescheduled_or_recovered_marker"` | - | 探针标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | kill_runner at pre_job (queued phase) |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | queued_escape_seconds le 600 | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
| 2 | queued_stall_beyond_window_detected = true | negative | - | ✅ GENUINE | fault_injection 在 queued 期间 kill runner，平台调度行为真实 |
| 3 | post_recovery_new_job_scheduled = true | positive | - | ✅ GENUINE | runner 恢复后平台恢复正常调度 |
---
