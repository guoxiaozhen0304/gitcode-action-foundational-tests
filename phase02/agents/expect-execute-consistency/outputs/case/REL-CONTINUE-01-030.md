# REL-CONTINUE-01-030
- **标题**: continue-on-error=true——job 失败后 workflow 不应终止
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**continue-on-error=true 时 job 失败不阻断后续 job**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-030
通过标准：
1. job_a 状态=failure
2. job_b 状态=success
3. workflow 不应整体 failure

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | fail step (job_a) | `exit 1` | continue-on-error: true | 真实失败，exit code 1 |
| 2 | success step (job_b) | `echo job_b executed` | - | 普通输出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_a_status = failure | positive | - | ✅ GENUINE | `exit 1` 真实产生失败 |
| 2 | job_b_status = success | positive | - | ✅ GENUINE | job_b 在 job_a 的 continue-on-error 后执行，真实测试容错语义 |
| 3 | workflow_status = success | positive | - | ✅ GENUINE | continue-on-error 使 workflow 终态为 success |
---
