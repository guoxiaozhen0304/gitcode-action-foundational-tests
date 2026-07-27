# REL-STATE-01-059
- **标题**: 运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-071
通过标准：
1. run 终态 status=completed、conclusion=success
2. 全部 job 终态后 ≤120s 内 run 收敛
3. 状态序列单调无抖动

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step one (job_1) | `sleep 60` | — | 持有 runner 60 秒 |
| 2 | sleep step two (job_2) | `sleep 60` | — | 持有 runner 60 秒 |
| 3 | sleep step three (job_3) | `sleep 60` | — | 持有 runner 60 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_conclusion = success | positive | — | ✅ GENUINE | 3 个并行 job 各 `sleep 60`，全部成功后由平台聚合 run 级 conclusion，真实测试多 job 收敛 |
| 2 | run_status_after_jobs_terminal = in_progress | negative | — | ✅ GENUINE | 验证 job 全部终态后 run 不应仍为 in_progress |
| 3 | convergence_seconds ≤ 120 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 4 | status_sequence_monotonic = true | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
