# USE-STAT-01-002
- **标题**: 使用 success() 带括号时报错应提示 GitCode 括号差异
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**使用 success() 带括号时报错应提示 GitCode 括号差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-004
通过标准：
1. 不应静默通过校验
2. 报错中应包含括号差异提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step with brackets | `echo "hello"` | `if: ${{ success() }}` | 预期报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | `if: ${{ success() }}` 含 `${{ }}` 表达式，success() 括号写法由平台求值 | ✅ GENUINE | 表达式求值涉及平台真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错括号差异提示 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定报错内容 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
