# COMPAT-EXPR-01-014

- **标题**: always() 带括号与不带括号的兼容性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**always() 带括号与不带括号的兼容性差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=positive, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Step with parens | `echo "with_parens"` | ${{ always() }} | ✅ GENUINE |
| 2 | Step without parens | `echo "without_parens"` | ${{ always }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-always-paren:
    name: Test always with/without parens
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Step with parens
        if: ${{ always() }}
        run: |
          echo "with_parens"
      - name: Step without parens
        if: ${{ always }}
        run: |
          echo "without_parens"
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
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | error_message | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---