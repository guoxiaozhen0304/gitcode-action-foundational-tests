# COMPAT-PERM-01-006

- **标题**: job 级 permissions 字段的支持度与降级方式（权限不得宽于声明）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**job 级 permissions 字段的支持度与降级方式（权限不得宽于声明）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-053

通过标准：
1. type=negative, target=run_status, eval=llm_assisted
2. type=positive, target=save_result, eval=llm_assisted
3. type=nonfunctional, target=save_result, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mark if job ran | `echo "JOB_LEVEL_PERM_JOB_RAN"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  probe:
    name: Probe job level permissions field
    permissions:
      contents: write
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mark if job ran
        run: |
          echo "JOB_LEVEL_PERM_JOB_RAN"
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
| 1 | run_status | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | save_result | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | save_result | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---