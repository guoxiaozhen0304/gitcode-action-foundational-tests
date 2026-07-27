# USE-RUN-01-002
- **标题**: 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**使用单标签 ubuntu-latest 时报错应给出三段式格式指引**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-006
通过标准：
1. 不应无限 queued 且无提示
2. 报错中应包含三段式或 default 等关键词

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step | `echo "hello"` | 无 | 预期平台对单标签写法报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | 步骤为纯 echo，但单标签 runs-on 校验由平台决定 | ✅ GENUINE | 平台对 runs-on 标签格式的校验是真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错格式指引内容 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定报错内容 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
