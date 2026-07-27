# REL-LATENCY-01-050-V2

- **标题**: 调度延迟压力——并发 20 个 job 的排队延迟与完成率
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**调度延迟压力——并发 20 个 job 的排队延迟与完成率**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-050

通过标准：
1. type=positive, target=completed_jobs_count, equals=20
2. type=nonfunctional, target=max_queued_time_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep 60s | `sleep 60` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: latency pressure job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        index: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    steps:
      - name: sleep 60s
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
| 1 | completed_jobs_count | positive | equals=20 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | max_queued_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---