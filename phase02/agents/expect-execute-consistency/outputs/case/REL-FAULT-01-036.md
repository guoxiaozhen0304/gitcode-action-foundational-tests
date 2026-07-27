# REL-FAULT-01-036
- **标题**: 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**runner 与平台心跳分区 60s 恢复后续跑完成**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-080
通过标准：
1. job 终态=success 且日志含分区后标记
2. 分区期间不应被判 failure
3. 心跳判死阈值观测

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | pre partition marker step | `echo "pre_partition_marker"` | - | 分区前标记 |
| 2 | long work step | `sleep 180` | - | 长耗时（分区注入点） |
| 3 | post partition marker step | `echo "post_partition_marker"` | - | 分区后标记 |
| 4 | final step | `echo "job_completed_marker"` | - | 完成标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | network_partition 60s at step 2 (runner→platform) |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | - | ✅ GENUINE | sleep 是真实命令；fault_injection 注入心跳分区 |
| 2 | run_logs contains "post_partition_marker" | positive | - | ✅ GENUINE | 分区恢复后步骤输出，作为续跑探针 |
| 3 | job_status = failure | negative | - | ✅ GENUINE | 不应因 60s 分区而 failure |
| 4 | heartbeat_death_threshold_observation = recorded | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
