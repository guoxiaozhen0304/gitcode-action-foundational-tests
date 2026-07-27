# USE-LOG-01-001

- **标题**: 多 step 日志按时间线组织且边界清晰
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**多 step 日志按时间线组织且边界清晰**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-017

通过标准：
1. type=positive, target=run_logs, contains="step one prepare"
2. type=nonfunctional, target=ui_layout, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | step one prepare | `echo "prepare done"` |  | ❌ VACUOUS |
| 2 | step two build | `echo "build done"` |  | ❌ VACUOUS |
| 3 | step three test | `echo "test done"` |  | ✅ GENUINE |
| 4 | step four package | `echo "package done"` |  | ❌ VACUOUS |
| 5 | step five summary | `echo "summary done"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  multi-step:
    name: multi step log clarity
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: step one prepare
        run: |
          echo "prepare done"
      - name: step two build
        run: |
          echo "build done"
      - name: step three test
        run: |
          echo "test done"
      - name: step four package
        run: |
          echo "package done"
      - name: step five summary
        run: |
          echo "summary done"
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
| 1 | run_logs | positive | contains=step one prepare | ❌ MISSING_SOURCE | step one prepare: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | ui_layout | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — MISSING_SOURCE**❌: step one prepare: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---