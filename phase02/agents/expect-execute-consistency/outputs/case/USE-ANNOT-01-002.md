# USE-ANNOT-01-002
- **标题**: ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转**
- 触发事件: `pull_request`
- 规格引用: INTENT-USE-021
通过标准：
1. annotation 是否包含准确的文件路径、行号、错误信息
2. annotation 颜色是否符合语义（error 红色、warning 黄色）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout | uses: checkout | - | 拉取代码 |
| 2 | emit annotation | `echo "::error file=README.md,line=1::Test error annotation"` | - | 输出 workflow commands |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | pr_ui | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 辅助判定 PR 页面 annotation 展示效果 |

### 问题
(无 — 两条断言均为 LLM_DEPENDENT，跳过评估。workflow 结构包含 uses: checkout + echo workflow commands，为 annotation 产生提供了 stimulus。)
---
