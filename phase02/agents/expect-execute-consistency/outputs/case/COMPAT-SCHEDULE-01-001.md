# COMPAT-SCHEDULE-01-001
- **标题**: schedule cron 按 UTC 时间触发
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule cron 按 UTC 时间触发**
- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-013
通过标准：
1. [正向] schedule 事件能正常触发 workflow
2. [非功能] 触发时间应与 UTC 解释一致

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo schedule time | `echo "SCHEDULE_TRIGGER_OK"` → `echo "Current UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"` | - | `SCHEDULE_TRIGGER_OK`, `Current UTC: <timestamp>` |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 步骤含 `$(date -u ...)` 实质命令输出 UTC 时间，非纯 echo |
| 2 | run_event | positive | equals=schedule | ✅ GENUINE | 断言事件与 trigger.event=schedule 一致 |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：需 LLM 验证触发时间按 UTC 解释 |

---
