# COMPAT-SCHEDULE-01-004
- **标题**: schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认**
- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-051
通过标准：
1. [正向] 自动停用策略有无得到确定结论
2. [负向] 不应存在未文档化的静默停用
3. [正向] 触发延迟可观测（计划 vs 实际入队时间）
4. [非功能] 结论文档化并回写 Parity Matrix

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Record actual trigger time | `date -u +"ACTUAL_TRIGGER_UTC=%Y-%m-%dT%H:%M:%SZ"` → `echo "SCHEDULE_PROBE_DONE"` | - | `ACTUAL_TRIGGER_UTC=<timestamp>`, `SCHEDULE_PROBE_DONE` |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="SCHEDULE_PROBE_DONE" | ✅ GENUINE | 步骤先执行 `date -u` 实质命令输出 UTC 触发时间再 echo 哨兵 |
| 2 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 长期观察评估静默停用 |
| 3 | run_list | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：比对 ACTUAL_TRIGGER_UTC 与计划时间 |

---
