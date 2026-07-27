# USE-INPT-01-002
- **标题**: 使用 boolean 类型 input 时报错应提示仅支持 string
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**使用 boolean 类型 input 时报错应提示仅支持 string**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-008
通过标准：
1. 不应静默降级为 string
2. 报错中应包含 string 与类型转换相关提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo input | `echo "dry_run=${{ inputs.dry_run }}"` | 无 | 预期校验阶段报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | 步骤含 `${{ inputs.dry_run }}` 表达式但 input type=boolean 非法 | ✅ GENUINE | 平台对不合规 input type 的校验是真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 辅助判定报错内容 | 🔶 LLM_DEPENDENT | 需 LLM 语义判定报错是否包含 string 类型转换提示 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
