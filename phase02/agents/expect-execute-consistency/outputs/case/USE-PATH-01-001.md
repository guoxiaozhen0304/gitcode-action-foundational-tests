# USE-PATH-01-001
- **标题**: paths 300 文件上限在文档与行为中一致且明示
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**paths 300 文件上限在文档与行为中一致且明示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-015
通过标准：
1. 文档 paths 章节顶部或注意块中是否有 300 文件上限提示
2. 超出上限时调试日志是否提示 paths 过滤超出文件上限

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | workflow: null | 无 workflow 步骤 | — | 纯文档分析 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation eval=llm_assisted | nonfunctional | LLM 判定文档 300 上限提示 | 🔶 LLM_DEPENDENT | 唯一断言为 LLM 辅助判定 |

### 问题
唯一断言为 nonfunctional + llm_assisted，无 workflow 执行步骤，完全依赖 LLM 判定文档质量。
---
