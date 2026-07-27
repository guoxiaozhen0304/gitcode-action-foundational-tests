# REL-VCJOB-01-001

- **标题**: 【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归**

- 触发事件: `manual`
- 规格引用: INTENT-REL-089

通过标准：
1. type=positive, target=vcjob_parse_status, equals=success
2. type=positive, target=vcjob_run_status, equals=Running
3. type=negative, target=vcjob_field_handling, eval=llm_assisted

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
| 1 | vcjob_parse_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | vcjob_run_status | positive | equals=Running | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | vcjob_field_handling | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---