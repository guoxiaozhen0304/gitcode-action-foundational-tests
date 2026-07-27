# COMP-CTX-01-054

- **标题**: pull_request 触发下 inputs 上下文求值裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request 触发下 inputs 上下文求值裁定**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-020

通过标准：
1. type=positive, target=run_logs, must_contain="INPUT_PR_ID="
2. type=nonfunctional, target=inputs_eval, eval=llm_assisted
3. type=negative, target=inputs_determinism, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo inputs reference | `echo "INPUT_PR_ID=${{ inputs.pr_id }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  probe:
    name: Probe inputs context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo inputs reference
        run: |
          echo "INPUT_PR_ID=${{ inputs.pr_id }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `maintainer` |
| Repo 环境 | `pr-default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=INPUT_PR_ID= | ✅ GENUINE | INPUT_PR_ID=: GENUINE |
| 2 | inputs_eval | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | inputs_determinism | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---