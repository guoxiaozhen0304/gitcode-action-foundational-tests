# COMPAT-VARS-01-005
- **标题**: vars 在条件表达式 if 中的可用性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 在条件表达式 if 中的可用性差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [正向] 若支持 vars，if 条件正确求值并控制步骤执行
2. [负向] 不通过 vars 在 if 中被静默视为空字符串

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Step always runs | `echo "always"` | - | `always` |
| 2 | Step conditional on vars | `echo "feature_enabled"` | `if: ${{ vars.ENABLE_FEATURE == 'true' }}` | `feature_enabled` (条件满足时) |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认条件步骤是否执行 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 vars 未被静默视为空 |

---
