# USE-UNKN-01-004
- **标题**: 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-037
通过标准：
1. 样本独有且文档未提的 key 每多 1 个即一条缺陷

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
| 1 | documentation 确定性校验：样本 YAML key 与文档合法 key 集合 diff | negative | 确定性文档/样本集合 diff | ✅ COVERED | 确定性文档校验 |
---
