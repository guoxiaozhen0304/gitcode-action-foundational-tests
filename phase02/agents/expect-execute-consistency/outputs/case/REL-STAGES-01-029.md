# REL-STAGES-01-029
- **标题**: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-029
通过标准：
1. 失败 job 状态 = failure
2. 同阶段其余 jobs 状态 ∈ {cancelled, skipped}

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | fail step (job_a) | `exit 1` | — | job_a 主动失败 |
| 2 | sleep step (job_b) | `sleep 30` | — | 持有 runner 等待被取消 |
| 3 | sleep step (job_c) | `sleep 30` | — | 持有 runner 等待被取消 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | — | ✅ GENUINE | `exit 1` 真实触发 job_a 失败，`fail_fast: true` 条件下平台应取消同阶段 job_b 和 job_c |
| 2 | cancelled_jobs_count ≥ 2 | positive | — | ✅ GENUINE | `sleep 30` 真实运行留出取消窗口，harness 验证 job_b 和 job_c 被取消 |
---
