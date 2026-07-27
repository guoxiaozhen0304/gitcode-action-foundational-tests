# REL-LOGPERF-01-052

- **标题**: 日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-084

通过标准：
1. type=positive, target=streaming_log_is_prefix_of_final, equals=true
2. type=nonfunctional, target=first_line_visibility_seconds
3. type=nonfunctional, target=p95_catchup_latency_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | emit timestamped lines st | `for i in $(seq 1 120); do echo "TS_$(date +%s)_LINE_$i"; sleep 5; done` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: streaming log probe job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 20
    steps:
      - name: emit timestamped lines step
        run: |
          for i in $(seq 1 120); do echo "TS_$(date +%s)_LINE_$i"; sleep 5; done
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
| 1 | streaming_log_is_prefix_of_final | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | first_line_visibility_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | p95_catchup_latency_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---