# REL-FAULT-01-039

- **标题**: 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-082

通过标准：
1. type=nonfunctional, target=queued_escape_seconds
2. type=negative, target=queued_stall_beyond_window_detected, equals=true
3. type=positive, target=post_recovery_new_job_scheduled, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | probe step | `echo "rescheduled_or_recovered_marker"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: queued runner offline probe job
    runs-on: [self-hosted, arch=x64, group=006]
    timeout-minutes: 30
    steps:
      - name: probe step
        run: |
          echo "rescheduled_or_recovered_marker"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'pre_job', 'action': 'kill_runner', 'params': {'phase': 'queued', 'target': 'only_matching_runner', 'method': 'stop_agent_process'}, 'recovery_expectation': 'reschedule_or_bounded_explicit_failure; pool_recovers_after_runner_rejoin'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | queued_escape_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | queued_stall_beyond_window_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | post_recovery_new_job_scheduled | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---