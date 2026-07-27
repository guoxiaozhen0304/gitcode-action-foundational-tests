# COMPAT-EXPR-01-009

- **标题**: loose equality 跨类型强制求值差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**loose equality 跨类型强制求值差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-009

通过标准：
1. type=positive, target=run_logs, must_contain="STRING_EQ_NUMBER="
2. type=positive, target=run_logs, must_contain="STRING_EQ_BOOL="
3. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Compare string one and nu | `if ${{ '1' == 1 }}; then   echo "STRING_EQ_NUMBER=true" else   echo "STRING_EQ_N` |  | ✅ GENUINE |
| 2 | Compare string true and b | `if ${{ 'true' == true }}; then   echo "STRING_EQ_BOOL=true" else   echo "STRING_` |  | ✅ GENUINE |
| 3 | Compare number zero and s | `if ${{ 0 == '0' }}; then   echo "ZERO_EQ_ZERO=true" else   echo "ZERO_EQ_ZERO=fa` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-loose-eq:
    name: Test loose equality cross type coercion
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare string one and number one
        run: |
          if ${{ '1' == 1 }}; then
            echo "STRING_EQ_NUMBER=true"
          else
            echo "STRING_EQ_NUMBER=false"
          fi
      - name: Compare string true and boolean true
        run: |
          if ${{ 'true' == true }}; then
            echo "STRING_EQ_BOOL=true"
          else
            echo "STRING_EQ_BOOL=false"
          fi
      - name: Compare number zero and string zero
        run: |
          if ${{ 0 == '0' }}; then
            echo "ZERO_EQ_ZERO=true"
          else
            echo "ZERO_EQ_ZERO=false"
          fi
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
| 1 | run_logs | positive | must_contain=STRING_EQ_NUMBER= | ✅ GENUINE | STRING_EQ_NUMBER=: GENUINE |
| 2 | run_logs | positive | must_contain=STRING_EQ_BOOL= | ✅ GENUINE | STRING_EQ_BOOL=: GENUINE |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---