# REL-STATE-01-058
- **标题**: Runner 状态机正确性——空闲/运行/离线转换与时序一致性
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner 状态机正确性——空闲/运行/离线转换与时序一致性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-058
通过标准：
1. 状态序列正确
2. idle→running ≤30s（非功能）
3. running→idle ≤60s（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 60` | — | 持有 runner 60 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | state_sequence = idle_running_idle | positive | — | ✅ GENUINE | `sleep 60` 真实命令使 job 运行 60 秒，产生完整的 idle→running→idle 状态转换，由 harness 外部轮询观测 |
| 2 | idle_to_running_seconds ≤ 30 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 3 | running_to_idle_seconds ≤ 60 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
