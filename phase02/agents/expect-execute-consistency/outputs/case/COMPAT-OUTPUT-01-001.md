# COMPAT-OUTPUT-01-001

- **标题**: 跨 Job 引用未声明 output 时返回空值的差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**跨 Job 引用未声明 output 时返回空值的差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-006

通过标准：
1. type=positive, target=run_status, equals=success, eval=llm_assisted
2. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Set output | `echo "declared_key=value_a" >> $ATOMGIT_OUTPUT` |  | ❌ VACUOUS |
| 2 | Echo outputs | `echo "declared=${{ needs.job-a.outputs.declared_key }}" echo "undeclared=${{ nee` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-a:
    name: Job A declare output
    runs-on: [ubuntu-latest, x64, small]
    outputs:
      declared_key: value_a
    steps:
      - name: Set output
        run: |
          echo "declared_key=value_a" >> $ATOMGIT_OUTPUT
  job-b:
    name: Job B reference outputs
    runs-on: [ubuntu-latest, x64, small]
    needs: job-a
    steps:
      - name: Echo outputs
        run: |
          echo "declared=${{ needs.job-a.outputs.declared_key }}"
          echo "undeclared=${{ needs.job-a.outputs.undeclared_key }}"
          echo "done"
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
| 1 | run_status | positive | equals=success | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---