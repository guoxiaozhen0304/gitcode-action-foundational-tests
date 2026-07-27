# REL-TIMEOUT-01-010
- **标题**: 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-010
通过标准：
1. job 状态 = failure
2. 日志含 timeout 信息

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 21660` | — | 运行 361 分钟，超出默认 timeout |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | — | ✅ GENUINE | `sleep 21660` 未声明 `timeout-minutes`，使用默认 360 分钟，超出后真实触发超时终止 |
| 2 | run_logs contains "timeout" | positive | — | ✅ GENUINE | 平台默认超时终止产生 timeout 日志 |
---
