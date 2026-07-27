# USE-VARS-01-001
- **标题**: vars 上下文在文档与样本中的声明必须一致
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**vars 上下文在文档与样本中的声明必须一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-014
通过标准：
1. 若支持，文档示例可运行且样本注释已移除已知不支持
2. 若不支持，文档中不应出现 vars 使用示例

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | workflow: null | 无 workflow 步骤 | — | 纯文档/样本一致性分析 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation eval=llm_assisted | nonfunctional | LLM 判定文档与样本 vars 声明一致性 | 🔶 LLM_DEPENDENT | 唯一断言为 LLM 辅助判定 |

### 问题
唯一断言为 nonfunctional + llm_assisted，无 workflow 执行步骤，完全依赖 LLM 判定文档-样本一致性。
---
