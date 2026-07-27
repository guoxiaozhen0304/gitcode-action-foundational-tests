# REL-LONG-01-043
- **标题**: 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-043
通过标准：
1. job 状态 = success（在 360 分钟 timeout 内完成）
2. 心跳日志间隔 ≤60 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | heartbeat run | `for i in $(seq 1 350); do echo heartbeat $i; sleep 60; done` | — | 350 行心跳日志，总计约 350 分钟 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | — | ✅ GENUINE | step 使用 `seq 1 350` 和 `sleep 60` 真实运行约 350 分钟，确实测试 timeout-minutes=360 边界 |
| 2 | heartbeat_interval_seconds ≤ 60 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
