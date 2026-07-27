# COMPAT-VARS-01-006
- **标题**: vars 在 Action 中的可用性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**vars 在 Action 中的可用性差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-022
通过标准：
1. [正向] 若支持 vars，Action 的 with 参数正确接收值
2. [负向] 不通过 vars 在 Action 中被静默视为空字符串

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use vars in action | `uses: checkout` with `ref: ${{ vars.ACTION_VAR }}` | - | checkout action 内部日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 action with 参数是否正确接收 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 vars 未被静默视为空 |

---
