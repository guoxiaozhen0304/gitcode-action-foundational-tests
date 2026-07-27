# COMP-UNKNOWN-01-005

- **标题**: 顶层 inputs 与 manual_override 字段的实际处理记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**顶层 inputs 与 manual_override 字段的实际处理记录**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-031

通过标准：
1. type=positive, target=run_logs, must_contain="TOP_INPUT="
2. type=nonfunctional, target=top_inputs_handling, eval=llm_assisted
3. type=negative, target=silent_ignore, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo top input | `echo "TOP_INPUT=${{ inputs.branch_name }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
inputs:
  branch_name:
    default: main
    manual_override: true
jobs:
  probe:
    name: Probe top level inputs
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo top input
        run: |
          echo "TOP_INPUT=${{ inputs.branch_name }}"
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
| 1 | run_logs | positive | must_contain=TOP_INPUT= | ✅ GENUINE | TOP_INPUT=: GENUINE |
| 2 | top_inputs_handling | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | silent_ignore | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---