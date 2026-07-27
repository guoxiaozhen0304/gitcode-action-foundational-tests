# COMPAT-VARS-01-002
- **标题**: vars 上下文若不支持应报错而非静默为空
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 上下文若不支持应报错而非静默为空**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [负向] 不应静默求值为空
2. [非功能] 报错信息应说明 vars 上下文不支持

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo vars unknown | `echo "unknown_var=${{ vars.UNKNOWN_VAR }}"` → `echo "done"` | - | `unknown_var=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估未知 vars 是否静默为空 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：需 LLM 评估报错提示内容 |

---
