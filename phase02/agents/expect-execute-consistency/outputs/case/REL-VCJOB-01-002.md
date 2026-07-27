# REL-VCJOB-01-002
- **标题**: 大规模 vcjob 并发提交（≥50）无丢失、无级联失败
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**大规模 vcjob 并发提交（≥50）无丢失、无级联失败**
- 触发事件: `manual` (platform-level batch operation)
- 规格引用: INTENT-REL-089
通过标准：
1. 提交数=任务记录数=终态数=50
2. 无静默丢失
3. 无级联失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (workflow: null) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | manual / platform_op: vcjob_batch_submit |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | submitted==recorded==terminal==50 | positive | vcjob_terminal_reconciliation | ❌ MISSING_SOURCE | workflow 为 null，无任何步骤产生 vcjob 对账结果 |
| 2 | 无静默丢失 | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
| 3 | 无级联失败 | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
唯一非 LLM 断言 MISSING_SOURCE，workflow 为空，YAML 无法驱动任何验证步骤。
---
