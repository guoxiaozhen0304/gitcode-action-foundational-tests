# REL-TIMEOUT-01-007

- **标题**: job timeout 边界值——359 分钟运行应在 360 分钟边界前完成
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**job timeout 边界值——359 分钟运行应在 360 分钟边界前完成**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-007

通过标准：
1. type=positive, target=job_status, equals=success
2. type=nonfunctional, target=job_duration_minutes

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | long sleep step | `sleep 21540` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: timeout test job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 360
    steps:
      - name: long sleep step
        run: |
          sleep 21540
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
| 1 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | job_duration_minutes | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---