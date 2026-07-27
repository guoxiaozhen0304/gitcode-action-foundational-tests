# USE-SCHED-01-001

- **标题**: schedule 不触发时的可观测提示（判定方式：llm_assisted）
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**schedule 不触发时的可观测提示（判定方式：llm_assisted）**

- 触发事件: `schedule`
- 规格引用: INTENT-USE-047

通过标准：
1. type=negative, target=ui, eval=llm_assisted
2. type=nonfunctional, target=ui, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | marker step | `echo "scheduled run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 0 * * *"
jobs:
  nightly:
    name: nightly schedule probe
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: marker step
        run: |
          echo "scheduled run"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `schedule` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | ui | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---