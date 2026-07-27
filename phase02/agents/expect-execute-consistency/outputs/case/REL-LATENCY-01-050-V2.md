# REL-LATENCY-01-050-V2
- **标题**: 调度延迟压力——并发 20 个 job 的排队延迟与完成率
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**并发 20 job 的排队延迟与完成率**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-050
通过标准：
1. 20 个 job 全部完成
2. 无饿死
3. 排队延迟可观测

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep 60s | `sleep 60` | matrix 20 实例 | 保持 job 运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_jobs_count = 20 | positive | - | ✅ GENUINE | sleep 是真实命令；matrix 20 实例并发调度 |
| 2 | max_queued_time_seconds le 300 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
---
