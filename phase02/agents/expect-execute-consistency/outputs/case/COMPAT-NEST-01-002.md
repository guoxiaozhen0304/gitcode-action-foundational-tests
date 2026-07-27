# COMPAT-NEST-01-002

- **标题**: workflow_call 嵌套层数 - 3 层越界应报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**workflow_call 嵌套层数 - 3 层越界应报错**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-015

通过标准：
1. type=negative, target=run_status, equals=success
2. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  call-level2:
    name: Call level 2 reusable workflow
    uses: ./.gitcode/workflows/level2.yml
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `reusable-workflow-3layer` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---