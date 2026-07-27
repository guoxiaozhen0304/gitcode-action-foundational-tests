# COMP-CALL-01-004

- **标题**: 未传 required secret 的 workflow_call 不应空值执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**未传 required secret 的 workflow_call 不应空值执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-030

通过标准：
1. type=negative, target=run_status, equals=success
2. type=negative, target=run_logs, must_contain="UPLOAD_DONE"
3. type=nonfunctional, target=error_message, eval=llm_assisted

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
  caller:
    name: Call reusable missing secret
    uses: ./.gitcode/workflows/reusable.yml
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `reusable-workflow-local` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | run_logs | negative | must_contain=UPLOAD_DONE | ❌ MISSING_SOURCE | UPLOAD_DONE: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

**断言 2 — MISSING_SOURCE**❌: UPLOAD_DONE: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---