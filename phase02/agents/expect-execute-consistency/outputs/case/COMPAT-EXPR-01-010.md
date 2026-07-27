# COMPAT-EXPR-01-010

- **标题**: loose equality null 与空字符串及零的等价性差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**loose equality null 与空字符串及零的等价性差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-009

通过标准：
1. type=positive, target=run_logs, must_contain="NULL_EQ_EMPTY="
2. type=positive, target=run_logs, must_contain="NULL_EQ_ZERO="
3. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Compare null and empty st | `if ${{ null == '' }}; then   echo "NULL_EQ_EMPTY=true" else   echo "NULL_EQ_EMPT` |  | ✅ GENUINE |
| 2 | Compare null and number z | `if ${{ null == 0 }}; then   echo "NULL_EQ_ZERO=true" else   echo "NULL_EQ_ZERO=f` |  | ✅ GENUINE |
| 3 | Compare null and false | `if ${{ null == false }}; then   echo "NULL_EQ_FALSE=true" else   echo "NULL_EQ_F` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-null-eq:
    name: Test loose equality with null
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare null and empty string
        run: |
          if ${{ null == '' }}; then
            echo "NULL_EQ_EMPTY=true"
          else
            echo "NULL_EQ_EMPTY=false"
          fi
      - name: Compare null and number zero
        run: |
          if ${{ null == 0 }}; then
            echo "NULL_EQ_ZERO=true"
          else
            echo "NULL_EQ_ZERO=false"
          fi
      - name: Compare null and false
        run: |
          if ${{ null == false }}; then
            echo "NULL_EQ_FALSE=true"
          else
            echo "NULL_EQ_FALSE=false"
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
| 1 | run_logs | positive | must_contain=NULL_EQ_EMPTY= | ✅ GENUINE | NULL_EQ_EMPTY=: GENUINE |
| 2 | run_logs | positive | must_contain=NULL_EQ_ZERO= | ✅ GENUINE | NULL_EQ_ZERO=: GENUINE |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---