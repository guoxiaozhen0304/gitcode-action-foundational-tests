# COMPAT-VARS-01-004
- **标题**: vars 与 env 同名时的优先级差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 与 env 同名时的优先级差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [正向] 若支持 vars，env 优先级高于 vars
2. [正向] shell 环境变量 $MY_VAR 返回 env_value

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo vars and env | `echo "shell_var=$MY_VAR"` → `echo "expr_var=${{ vars.MY_VAR }}"` → `echo "done"` | - | `shell_var=env_value`, `expr_var=var_value`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 shell_var 优先返回 env_value |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 expr_var 返回 var_value |

---
