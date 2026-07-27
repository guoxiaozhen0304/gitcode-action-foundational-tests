# REL-QUEUE-01-003
- **标题**: concurrency QUEUE 策略——超上限运行应排队等待
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**concurrency QUEUE 策略——超上限运行应排队等待**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-003
通过标准：
1. 4 个运行最终全部 completed(success)
2. 运行 3-4 不应被丢弃

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
| 1 | run_status = completed(success) | positive | — | ✅ GENUINE | `sleep 30` 真实命令 + `concurrency.max=2 exceed-action=QUEUE` 真实测试排队策略 |
| 2 | queued_count = 2 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
