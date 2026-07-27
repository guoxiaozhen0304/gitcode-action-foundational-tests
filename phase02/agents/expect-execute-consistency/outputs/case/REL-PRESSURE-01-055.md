# REL-PRESSURE-01-055
- **标题**: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-055
通过标准：
1. completed = 20
2. running 峰值不应 >5（非功能）
3. 总耗时 ≤15min（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 30` | — | 持有 runner 30 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count = 20 | positive | — | ✅ GENUINE | `sleep 30` 是真实命令，使 job 持有 runner 30 秒。20 次并发触发 + concurrency.max=5 + exceed-action=QUEUE 真实测试并发排队与完成 |
| 2 | max_running_count ≤ 5 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 3 | total_duration_seconds ≤ 900 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
