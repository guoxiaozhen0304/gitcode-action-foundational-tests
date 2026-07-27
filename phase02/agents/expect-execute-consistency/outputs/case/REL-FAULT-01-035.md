# REL-FAULT-01-035
- **标题**: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**download-artifact 时服务 503 应失败并报依赖服务错误**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-035
通过标准：
1. download-artifact step 状态=failure
2. 日志含 503 错误
3. job 状态=failure

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | download artifact step | `uses: download-artifact` name=missing-artifact | - | action 输出（含 503 错误） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | artifact download service 503 at step 1 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status = failure | positive | - | ✅ GENUINE | uses download-artifact action + 503 故障注入 |
| 2 | run_logs contains "503" | positive | - | ✅ GENUINE | action 内部输出 HTTP 503 响应 |
| 3 | job_status = failure | positive | - | ✅ GENUINE | 下载失败导致 job 失败 |
---
