# COMPAT-VARS-01-001
- **标题**: vars 上下文若支持应正确返回值
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 上下文若支持应正确返回值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [正向] vars.TEST_VAR 返回配置值

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo vars TEST_VAR | `echo "test_var=${{ vars.TEST_VAR }}"` → `echo "done"` | - | `test_var=hello_vars`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 步骤含 `${{ vars.TEST_VAR }}` 表达式，平台上下文求值即功能执行，非单纯 echo |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 test_var 值为 hello_vars |

---
