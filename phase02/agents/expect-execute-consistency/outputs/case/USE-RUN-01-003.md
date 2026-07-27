# USE-RUN-01-003

- **标题**: rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-049

通过标准：
1. type=nonfunctional, target=ui, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | fail step | `exit 1` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  flaky:
    name: failing job for rerun probe
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: fail step
        run: |
          exit 1
```

</details>

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
| 1 | ui | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---