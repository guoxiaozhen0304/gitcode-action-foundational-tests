# USE-LBL-01-001
- **标题**: runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-025
通过标准：
1. 不应无限 queued 且无提示
2. 错误信息中是否包含用户指定的标签文本

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step | `echo "hello"` | 无 | job 因 runner 标签不匹配而无法调度 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | 步骤代码虽仅为 echo，但 runner 标签不匹配的行为由平台调度器决定 | ✅ GENUINE | 平台调度匹配行为是真实行为，非步骤代码可自证 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 辅助判定报错内容 | 🔶 LLM_DEPENDENT | 需 LLM 语义判定报错是否包含标签原文与可用列表 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
