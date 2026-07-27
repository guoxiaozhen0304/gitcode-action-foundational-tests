# COMPAT-WCMD-01-001
- **标题**: ::add-mask:: 不被支持时应静默降级而非报错
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**::add-mask:: 不被支持时应静默降级而非报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-009
通过标准：
1. [正向] workflow 不因 add-mask 命令而失败
2. [负向] 不通过 add-mask 导致 workflow 报错中断

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use add-mask | `echo "::add-mask::MY_SECRET_VALUE"` → `echo "MY_SECRET_VALUE"` → `echo "done"` | - | `::add-mask::MY_SECRET_VALUE`, `MY_SECRET_VALUE`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success, eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 add-mask 是否导致失败 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估是否报错中断 |

---
