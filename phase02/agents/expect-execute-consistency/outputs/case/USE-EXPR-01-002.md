# USE-EXPR-01-002
- **标题**: 调用未知函数时报错应提示函数名错误与修正方向
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**调用未知函数时报错应提示函数名错误与修正方向**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-024
通过标准：
1. 不应静默通过
2. 报错中是否包含 unknownFunc 或未知函数字样

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | bad function | `echo "hello"` | `if: ${{ unknownFunc() }}` | 预期报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | `if: ${{ unknownFunc() }}` 含 `${{ }}` 表达式调用未知函数 | ✅ GENUINE | 表达式求值涉及平台真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 辅助判定报错内容 | 🔶 LLM_DEPENDENT | 需 LLM 语义判定报错是否包含 unknownFunc 字样 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
