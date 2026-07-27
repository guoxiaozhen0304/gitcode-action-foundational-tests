# USE-DOC-01-001
- **标题**: stages 与 post 概念在迁移文档中具备可发现性
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**stages 与 post 概念在迁移文档中具备可发现性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-011
通过标准：
1. 迁移相关页面有 stages/post 的入口链接
2. 说明是否包含 GitCode 特有/GitHub 无此概念等显式差异标注

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (无 workflow) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 辅助判定文档可发现性 |

### 问题
(无 — 全部断言为 LLM_DEPENDENT)
---
