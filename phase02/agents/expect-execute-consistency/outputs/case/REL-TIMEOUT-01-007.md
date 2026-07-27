# REL-TIMEOUT-01-007
- **标题**: job timeout 边界值——359 分钟运行应在 360 分钟边界前完成
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**job timeout 边界值——359 分钟运行应在 360 分钟边界前完成**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-007
通过标准：
1. job 状态 = success
2. job 时长 ≤359 分钟（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | long sleep step | `sleep 21540` | — | 运行约 359 分钟（21540 秒） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | — | ✅ GENUINE | `sleep 21540`（=359 分钟）真实运行接近 `timeout-minutes=360` 边界，无失败路径 |
| 2 | job_duration_minutes ≤ 359 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
