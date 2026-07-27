# REL-TIMEOUT-01-009
- **标题**: 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-009
通过标准：
1. job 状态 = failure
2. 实际运行时长 60±10 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | long sleep step | `sleep 120` | — | 运行 120 秒，超出 timeout-minutes=1 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | — | ✅ GENUINE | `sleep 120` 超出 `timeout-minutes=1`，真实触发平台超时终止 |
| 2 | job_duration_seconds ≤ 70 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
