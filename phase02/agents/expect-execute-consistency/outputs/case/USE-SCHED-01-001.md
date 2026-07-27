# USE-SCHED-01-001
- **标题**: schedule 不触发时的可观测提示（判定方式：llm_assisted）
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**schedule 不触发时的可观测提示（判定方式：llm_assisted）**
- 触发事件: `schedule`
- 规格引用: INTENT-USE-047
通过标准：
1. schedule 未触发时平台不应完全静默
2. workflow 列表应显示下次预计触发时间字段
3. 跳过的触发应有原因记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "scheduled run"` | 无 | 标记日志（仅在触发时输出） |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui eval=llm_assisted | negative | LLM 判定不触发时的静默/可观测性 | 🔶 LLM_DEPENDENT | 完全依赖 LLM 辅助判定 |
| 2 | ui eval=llm_assisted | nonfunctional | LLM 判定 UI 区分 cron 写错与平台故障 | 🔶 LLM_DEPENDENT | 完全依赖 LLM 辅助判定 |

### 问题
两个断言均为 nonfunctional + llm_assisted，步骤仅有纯 echo 无平台行为验证，无法进行自动化判定。
---
