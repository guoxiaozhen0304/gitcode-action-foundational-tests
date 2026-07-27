# COMPAT-VARS-01-003
- **标题**: vars 项目级覆盖组织级的优先级差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 项目级覆盖组织级的优先级差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [正向] 若支持 vars，项目级值覆盖组织级值
2. [负向] 不通过组织级值错误地覆盖项目级值

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo vars | `echo "org_var=${{ vars.ORG_VAR }}"` → `echo "done"` | - | `org_var=proj_value`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认返回值覆盖优先级 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认未错误覆盖 |

---
