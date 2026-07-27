# COMPAT-EXPR-01-008

- **标题**: toJson 表达式输出格式差异（pretty-print vs compact）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**toJson 表达式输出格式差异（pretty-print vs compact）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-008

通过标准：
1. type=positive, target=run_logs, must_contain="key1"
2. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Output object via toJson | `echo '${{ toJson({'key1': 'value1', 'key2': 'value2'}) }}'` |  | ✅ GENUINE |
| 2 | Output array via toJson | `echo '${{ toJson(['a', 'b', 'c']) }}'` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-tojson:
    name: Test toJson output format
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Output object via toJson
        run: |
          echo '${{ toJson({'key1': 'value1', 'key2': 'value2'}) }}'
      - name: Output array via toJson
        run: |
          echo '${{ toJson(['a', 'b', 'c']) }}'
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
| 1 | run_logs | positive | must_contain=key1 | ✅ GENUINE | key1: GENUINE |
| 2 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---