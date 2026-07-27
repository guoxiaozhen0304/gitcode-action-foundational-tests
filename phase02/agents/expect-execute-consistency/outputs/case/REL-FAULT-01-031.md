# REL-FAULT-01-031

- **标题**: 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-031

通过标准：
1. type=positive, target=job_status, equals=failure
2. type=positive, target=run_logs, contains="step_one_marker"
3. type=negative, target=run_logs, contains="step_four_marker"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | step one | `echo step_one_marker` |  | ❌ VACUOUS |
| 2 | step two | `echo step_two_marker` |  | ❌ VACUOUS |
| 3 | step three | `sleep 30` |  | ✅ GENUINE |
| 4 | step four | `echo step_four_marker` |  | ❌ VACUOUS |
| 5 | step five | `echo step_five_marker` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: fault injection SIGKILL
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: step one
        run: |
          echo step_one_marker
      - name: step two
        run: |
          echo step_two_marker
      - name: step three
        run: |
          sleep 30
      - name: step four
        run: |
          echo step_four_marker
      - name: step five
        run: |
          echo step_five_marker
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'kill_runner', 'params': {'target_step': 3}, 'recovery_expectation': 'retry_and_succeed'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | run_logs | positive | contains=step_one_marker | ❌ VACUOUS | step_one_marker: VACUOUS (步骤仅 echo，未执行功能) |
| 3 | run_logs | negative | contains=step_four_marker | ❌ VACUOUS | step_four_marker: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 2 — VACUOUS**❌: step_one_marker: VACUOUS (步骤仅 echo，未执行功能)

**断言 3 — VACUOUS**❌: step_four_marker: VACUOUS (步骤仅 echo，未执行功能)

---