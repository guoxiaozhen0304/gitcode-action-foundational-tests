# USE-VARS-01-001

- **标题**: vars 上下文在文档与样本中的声明必须一致
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**vars 上下文在文档与样本中的声明必须一致**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-014

通过标准：
1. type=nonfunctional, target=documentation, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---