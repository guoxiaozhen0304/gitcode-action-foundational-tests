# REL-IGNORE-01-004
- **标题**: concurrency IGNORE 策略——超上限运行应直接执行
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**concurrency IGNORE 策略下超上限运行直接执行不排队**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-004
通过标准：
1. 4 个运行全部 completed(success)
2. 不应出现 queued 状态

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 30` | concurrency max=2 exceed-action=IGNORE | 保持 job 运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(success) | positive | - | ✅ GENUINE | sleep 是真实命令；IGNORE 策略是真实平台功能 |
| 2 | run_status = queued | negative | - | ✅ GENUINE | IGNORE 策略下不应有排队 |
---
