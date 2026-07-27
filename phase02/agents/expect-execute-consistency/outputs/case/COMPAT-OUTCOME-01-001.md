# COMPAT-OUTCOME-01-001

- **标题**: continue-on-error false 时 outcome 与 conclusion 应均为 failure
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**continue-on-error false 时 outcome 与 conclusion 应均为 failure**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-035

通过标准：
1. type=positive, target=step_status, equals=failure, eval=llm_assisted
2. type=positive, target=step_conclusion, equals=failure, eval=llm_assisted
3. type=positive, target=run_status, equals=failure, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | failing step | `exit 1` |  | ✅ GENUINE |
| 3 | check status | `echo "Check step outcome and conclusion"` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  outcome-false:
    name: Test outcome with continue on error false
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: failing step
        continue-on-error: false
        run: |
          exit 1
      - name: check status
        if: ${{ always() }}
        run: |
          echo "Check step outcome and conclusion"
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
| 1 | step_status | positive | equals=failure | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | step_conclusion | positive | equals=failure | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_status | positive | equals=failure | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---