# REL-NEEDS-01-025
- **标题**: needs 失败传播——上游 job 失败时下游 job 应被 skip
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**needs 失败传播——上游 job 失败时下游 job 应被 skip**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-025
通过标准：
1. job_a 状态 = failure
2. job_b 状态 = skipped

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | fail step (job_a) | `exit 1` | — | 主动退出 1，job_a 失败 |
| 2 | should be skipped (job_b) | `echo this should not run` | needs: job_a | 此步骤不应执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status = failure | positive | — | ✅ GENUINE | `exit 1` 真实触发 job 失败，有明确失败路径 |
| 2 | job_b_status = skipped | positive | — | ✅ GENUINE | job_b 通过 `needs: job_a` 真实依赖 job_a 的结果，由平台 needs 机制决定是否跳过 |
---
