# USE-YAML-01-002
- **标题**: YAML 缩进错误时报错应指出具体行号与列号
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**YAML 缩进错误时报错应指出具体行号与列号**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-022
通过标准：
1. 不应仅报泛化 YAML parse error
2. 报错中是否包含行号与列号

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step one | `echo "hello"` | 无 | 步骤因 YAML 缩进错误可能无法解析 |
| 2 | step two | `echo "world"` | 无 | 错误缩进导致 YAML 解析失败 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | YAML 缩进错误 → 平台 YAML 解析校验 | ✅ GENUINE | 平台 YAML 解析校验是真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错行号与列号信息 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定报错内容 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
