# REL-STATE-01-059

- **标题**: 运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-071

通过标准：
1. type=positive, target=run_conclusion, equals=success
2. type=negative, target=run_status_after_jobs_terminal, equals=in_progress
3. type=nonfunctional, target=convergence_seconds
4. type=nonfunctional, target=status_sequence_monotonic, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step one | `sleep 60` |  | ✅ GENUINE |
| 2 | sleep step two | `sleep 60` |  | ✅ GENUINE |
| 3 | sleep step three | `sleep 60` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job_1:
    name: parallel job one
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step one
        run: |
          sleep 60
  job_2:
    name: parallel job two
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step two
        run: |
          sleep 60
  job_3:
    name: parallel job three
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step three
        run: |
          sleep 60
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
| 1 | run_conclusion | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_status_after_jobs_terminal | negative | equals=in_progress | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | convergence_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | status_sequence_monotonic | nonfunctional | equals=true | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---