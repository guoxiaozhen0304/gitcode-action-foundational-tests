# REL-SCHED-01-057
- **标题**: 资源调度状态一致性——空闲 runner 存在时 job 不应死等
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**资源调度状态一致性——空闲 runner 存在时 job 不应死等**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-057
通过标准：
1. 10 次全部 queued→running ≤60s（非功能）
2. 平均 ≤30s（非功能）

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
| 1 | max_queued_to_running_seconds ≤ 60 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 2 | avg_queued_to_running_seconds ≤ 30 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
