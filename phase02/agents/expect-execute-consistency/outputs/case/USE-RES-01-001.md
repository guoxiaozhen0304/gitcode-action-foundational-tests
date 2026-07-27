# USE-RES-01-001
- **标题**: runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-012
通过标准：
1. 所有独立环境变量示例使用 ATOMGIT_ 前缀
2. 正文中不应出现未标注为 GitHub 对照的 GITHUB_ 残留措辞

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
| 1 | documentation eval=llm_assisted | negative | LLM 判定 GITHUB_ 前缀残留 | 🔶 LLM_DEPENDENT | 唯一断言为 LLM 辅助判定 |

### 问题
唯一断言为 nonfunctional + llm_assisted，无 workflow 执行步骤，完全依赖 LLM 判定文档质量。
---
