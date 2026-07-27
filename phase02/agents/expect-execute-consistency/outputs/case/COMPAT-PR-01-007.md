# COMPAT-PR-01-007
- **标题**: pull_request 不支持的 activity type（labeled）不应静默退化
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request 不支持的 activity type（labeled）不应静默退化**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-038
通过标准：
1. [负向] types 含 labeled 不应被静默忽略而退化为全量触发
2. [正向] 解析期报错列出 GitCode 合法的 4 种 types（open/reopen/update/merge）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Should not run for unlabeled activity | `echo "LABELED_TYPE_JOB_RAN"` | - | `LABELED_TYPE_JOB_RAN` |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 types 是否被静默忽略 |
| 2 | save_result | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估解析阶段报错内容 |

---
