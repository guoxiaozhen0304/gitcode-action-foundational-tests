# COMPAT-SHELL-01-003
- **标题**: Windows runner 默认 shell 差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Windows runner 默认 shell 差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-001
通过标准：
1. [正向] 默认 shell 正确执行 Windows 命令
2. [正向] 若默认 shell 不是 powershell，系统应给出明确说明

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo OS | `echo %OS%` → `echo "done"` | - | `%OS% 或 Windows_NT`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 shell 是否正确执行 Windows 命令 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 shell 说明信息 |

---
