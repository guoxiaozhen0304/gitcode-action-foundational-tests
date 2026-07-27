# REL-FAULT-01-031
- **标题**: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runner 被 SIGKILL 后已执行日志应保留且正确标记失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-031
通过标准：
1. job 状态=failure
2. step 1-2 日志完整
3. step 4 日志不应出现

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step one | `echo step_one_marker` | - | 标记行 |
| 2 | step two | `echo step_two_marker` | - | 标记行 |
| 3 | step three | `sleep 30` | - | kill 注入点 |
| 4 | step four | `echo step_four_marker` | - | 不应执行的标记 |
| 5 | step five | `echo step_five_marker` | - | 不应执行的标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | kill_runner at step 3 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | - | ✅ GENUINE | kill_runner 故障注入导致真实 job 失败 |
| 2 | run_logs contains "step_one_marker" | positive | - | ✅ GENUINE | step 1 在 kill 前真实执行，echo 输出作为可观测探针 |
| 3 | run_logs contains "step_four_marker" | negative | - | ✅ GENUINE | kill 发生在 step 3，step 4 不应有输出 |
---
