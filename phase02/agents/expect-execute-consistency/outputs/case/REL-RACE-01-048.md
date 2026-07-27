# REL-RACE-01-048
- **标题**: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-048
通过标准：
1. job A 状态 = cancelled
2. job B 状态 = skipped

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step (job_a) | `sleep 60` | — | 持有 runner 60 秒等待手动取消 |
| 2 | should not run (job_b) | `echo this should not run` | needs: job_a, if: failure() | 此步骤不应执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status = canceled | positive | — | ✅ GENUINE | `sleep 60` 真实命令为手动取消提供时间窗口，由外部取消操作真实触发 cancelled 状态 |
| 2 | job_b_status = skipped | positive | — | ✅ GENUINE | job_b 使用 `needs: job_a` + `if: failure()` 条件，测试 cancelled 状态下 failure() 的判定逻辑 |
---
