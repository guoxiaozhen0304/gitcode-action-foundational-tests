# REL-FAULT-01-036

- **标题**: 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-080

通过标准：
1. type=positive, target=job_status, equals=success
2. type=positive, target=run_logs, contains="post_partition_marker"
3. type=negative, target=job_status, equals=failure
4. type=nonfunctional, target=heartbeat_death_threshold_observation, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | pre partition marker step | `echo "pre_partition_marker"` |  | ❌ VACUOUS |
| 2 | long work step | `sleep 180` |  | ✅ GENUINE |
| 3 | post partition marker ste | `echo "post_partition_marker"` |  | ❌ VACUOUS |
| 4 | final step | `echo "job_completed_marker"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: heartbeat partition 60s job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 30
    steps:
      - name: pre partition marker step
        run: |
          echo "pre_partition_marker"
      - name: long work step
        run: |
          sleep 180
      - name: post partition marker step
        run: |
          echo "post_partition_marker"
      - name: final step
        run: |
          echo "job_completed_marker"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'network_partition', 'params': {'scope': 'runner_to_platform', 'duration_seconds': 60, 'inject_at_step': 2}, 'recovery_expectation': 'auto_recover_resume_and_success'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | run_logs | positive | contains=post_partition_marker | ❌ VACUOUS | post_partition_marker: VACUOUS (步骤仅 echo，未执行功能) |
| 3 | job_status | negative | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 4 | heartbeat_death_threshold_observation | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — VACUOUS**❌: post_partition_marker: VACUOUS (步骤仅 echo，未执行功能)

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---