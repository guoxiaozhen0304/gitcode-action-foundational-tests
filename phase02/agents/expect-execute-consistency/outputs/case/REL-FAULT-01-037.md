# REL-FAULT-01-037

- **标题**: 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-080

通过标准：
1. type=positive, target=outcome, equals=resumed_success_or_explicit_lost_with_attribution
2. type=negative, target=failure_attribution, equals=missing
3. type=nonfunctional, target=first_misjudge_or_death_threshold_seconds, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | pre partition marker step | `echo "pre_partition_marker"` |  | ❌ VACUOUS |
| 2 | long work step | `sleep 420` |  | ✅ GENUINE |
| 3 | post partition marker ste | `echo "post_partition_marker"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: heartbeat partition 300s job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 30
    steps:
      - name: pre partition marker step
        run: |
          echo "pre_partition_marker"
      - name: long work step
        run: |
          sleep 420
      - name: post partition marker step
        run: |
          echo "post_partition_marker"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'network_partition', 'params': {'scope': 'runner_to_platform', 'duration_seconds': 300, 'inject_at_step': 2}, 'recovery_expectation': 'auto_recover_or_explicit_lost_with_attribution; rerun_succeeds'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | outcome | positive | equals=resumed_success_or_explicit_lost_with_attribution | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | failure_attribution | negative | equals=missing | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | first_misjudge_or_death_threshold_seconds | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---