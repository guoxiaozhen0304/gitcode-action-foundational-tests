# USE-ANNOT-01-002

- **标题**: ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转**

- 触发事件: `pull_request`
- 规格引用: INTENT-USE-021

通过标准：
1. type=nonfunctional, target=pr_ui, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout | `checkout` |  | ✅ GENUINE |
| 2 | emit annotation | `echo "::error file=README.md,line=1::Test error annotation" echo "::warning file` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    types:
      - open
      - update
    branches: [main]
jobs:
  annot-pr:
    name: PR annotation test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout
        uses: checkout
      - name: emit annotation
        run: |
          echo "::error file=README.md,line=1::Test error annotation"
          echo "::warning file=README.md,line=2::Test warning annotation"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | pr_ui | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---