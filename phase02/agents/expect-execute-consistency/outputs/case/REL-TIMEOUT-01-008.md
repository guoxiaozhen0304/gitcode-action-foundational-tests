# REL-TIMEOUT-01-008
- **标题**: job timeout 越界触发——361 分钟应在 360 分钟被强制终止
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**job timeout 越界触发——361 分钟应在 360 分钟被强制终止**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-008
通过标准：
1. job 状态 = failure
2. 日志含 timeout 信息

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | long sleep step | `sleep 21660` | — | 运行约 361 分钟（21660 秒），超出 timeout-minutes=360 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | — | ✅ GENUINE | `sleep 21660`（=361 分钟）超出 `timeout-minutes=360`，真实触发平台超时终止机制，有明确失败路径 |
| 2 | run_logs contains "timeout" | positive | — | ✅ GENUINE | 平台超时终止产生的日志包含 "timeout"，由平台行为生成，非脚本 echo |
---
