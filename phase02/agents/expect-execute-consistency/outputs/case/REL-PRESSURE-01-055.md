# REL-PRESSURE-01-055

- **标题**: 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-055

通过标准：
1. type=positive, target=completed_count, equals=20
2. type=nonfunctional, target=max_running_count
3. type=nonfunctional, target=total_duration_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 30` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
concurrency:
  max: 5
  exceed-action: QUEUE
jobs:
  test:
    name: concurrency test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 30
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
| 1 | completed_count | positive | equals=20 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | max_running_count | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | total_duration_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---