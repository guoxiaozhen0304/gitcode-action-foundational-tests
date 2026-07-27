# REL-FAULT-01-037
- **标题**: 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**心跳分区 300s——行为确定可归因**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-080
通过标准：
1. 终态可归因：success 或 failure（失联）
2. 不应无归因说明失败或长期悬挂
3. 首次判死时间点记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | pre partition marker step | `echo "pre_partition_marker"` | - | 分区前标记 |
| 2 | long work step | `sleep 420` | - | 长耗时（分区注入点） |
| 3 | post partition marker step | `echo "post_partition_marker"` | - | 分区后标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | network_partition 300s at step 2 (runner→platform) |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | outcome = resumed_success_or_explicit_lost_with_attribution | positive | - | ✅ GENUINE | sleep 是真实命令；fault_injection 注入长时分区 |
| 2 | failure_attribution = missing | negative | - | ✅ GENUINE | 负向验证归因不缺失 |
| 3 | first_misjudge_or_death_threshold_seconds = recorded | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
