# REL-SCHED-01-058
- **标题**: schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性**
- 触发事件: `schedule`
- 规格引用: INTENT-REL-085
通过标准：
1. 触发次数 ≥23/24，每次 run 的 sha=默认分支 HEAD
2. 非默认分支不应产生任何 run
3. 同一计划时刻不应重复触发
4. 丢失率 ≤5%（非功能）
5. 触发延迟 P95 ≤300 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | tick step | `echo "schedule_tick $(date -u +%FT%TZ)"` | — | 输出每次触发的 UTC 时间戳 |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | runs_on_default_branch_head = true | positive | — | ✅ GENUINE | schedule trigger 真实由平台 cron 触发，`$(date -u +%FT%TZ)` 输出实际触发时刻，由 harness 验证 sha 归属 |
| 2 | duplicate_trigger_count = 0 | positive | — | ✅ GENUINE | 对账逻辑由 harness 比较触发时刻，step 输出时间戳提供真实数据 |
| 3 | non_default_branch_triggered = true | negative | — | ✅ GENUINE | 验证非默认分支不应触发 schedule |
| 4 | trigger_loss_rate_pct ≤ 5 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 5 | trigger_delay_p95_seconds ≤ 300 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
