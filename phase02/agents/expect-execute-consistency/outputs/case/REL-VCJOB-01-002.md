# REL-VCJOB-01-002

- **标题**: 大规模 vcjob 并发提交（≥50）无丢失、无级联失败
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**大规模 vcjob 并发提交（≥50）无丢失、无级联失败**

- 触发事件: `manual`
- 规格引用: INTENT-REL-089

通过标准：
1. type=positive, target=vcjob_terminal_reconciliation, equals=submitted==recorded==terminal==50
2. type=negative, target=vcjob_records, eval=llm_assisted
3. type=nonfunctional, target=cascading_failure, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `manual` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_terminal_reconciliation | positive | equals=submitted==recorded==terminal==50 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | vcjob_records | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | cascading_failure | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---