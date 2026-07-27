# USE-DIR-01-002
- **标题**: .github/workflows/ 下 workflow 未被识别时应给出目录差异提示
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**.github/workflows/ 下 workflow 未被识别时应给出目录差异提示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-001
通过标准：
1. 不应无任何提示地忽略 .github/workflows/ 下的文件
2. 提示信息中应包含 .gitcode/workflows 字样

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
| 1 | system_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定系统提示文本 |

### 问题
(无 — 断言为 LLM_DEPENDENT，跳过。本用例预期 .github/workflows/ 下文件被静默忽略，系统应发出提示，但提示质量需 LLM 评估，workflow 不参与该判定。)
---
