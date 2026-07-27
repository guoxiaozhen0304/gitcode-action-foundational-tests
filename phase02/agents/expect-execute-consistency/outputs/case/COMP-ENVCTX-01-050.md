# COMP-ENVCTX-01-050

- **标题**: env 优先级链 step 大于 job 大于 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**env 优先级链 step 大于 job 大于 workflow**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-050

通过标准：
1. type=positive, target=run_logs, must_contain="MY_VAR=step_value"
2. type=positive, target=run_logs, must_contain="JOB_VAR=job_value"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Step override | `echo "MY_VAR=$MY_VAR"` |  | ❌ VACUOUS |
| 2 | Job inherit | `echo "JOB_VAR=$MY_VAR"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
env:
  MY_VAR: workflow_value
jobs:
  verify:
    name: Verify env priority chain
    runs-on: [ubuntu-latest, x64, small]
    env:
      MY_VAR: job_value
    steps:
      - name: Step override
        env:
          MY_VAR: step_value
        run: |
          echo "MY_VAR=$MY_VAR"
      - name: Job inherit
        run: |
          echo "JOB_VAR=$MY_VAR"
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
| 1 | run_logs | positive | must_contain=MY_VAR=step_value | ❌ MISSING_SOURCE | MY_VAR=step_value: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=JOB_VAR=job_value | ❌ MISSING_SOURCE | JOB_VAR=job_value: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: MY_VAR=step_value: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: JOB_VAR=job_value: MISSING_SOURCE (无步骤产出此字符串)

---