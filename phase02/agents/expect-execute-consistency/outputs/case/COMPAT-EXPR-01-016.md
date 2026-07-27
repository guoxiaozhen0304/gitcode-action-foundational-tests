# COMPAT-EXPR-01-016

- **标题**: format() 花括号转义与字符串字面量引号规则边界
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**format() 花括号转义与字符串字面量引号规则边界**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-050

通过标准：
1. type=positive, target=run_logs, must_contain="PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Evaluate format brace esc | `echo "FMT_BRACE=${{ format('{{{0}}}', 'x') }}"` |  | ✅ GENUINE |
| 2 | Evaluate single quote esc | `echo "FMT_QUOTE=${{ format('it''s {0}', 'ok') }}" echo "PROBE_DONE"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe format escaping and literal quotes
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Evaluate format brace escaping
        run: |
          echo "FMT_BRACE=${{ format('{{{0}}}', 'x') }}"
      - name: Evaluate single quote escaping
        run: |
          echo "FMT_QUOTE=${{ format('it''s {0}', 'ok') }}"
          echo "PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=PROBE_DONE | ✅ GENUINE | PROBE_DONE: GENUINE |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---