# REL-FAULT-01-034

- **标题**: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-034

通过标准：
1. type=positive, target=job_status, equals=success
2. type=positive, target=run_logs, contains="cache miss"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | restore cache step | `cache` |  | ✅ GENUINE |
| 2 | subsequent step | `echo subsequent step executed` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: fault injection cache 503
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: restore cache step
        uses: cache
        with:
          path: node_modules
          key: cache-deps
      - name: subsequent step
        run: |
          echo subsequent step executed
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'concurrent_flood', 'params': {'service': 'cache', 'response': 503, 'target_step': 1}, 'recovery_expectation': 'graceful_degradation_cache_miss'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | run_logs | positive | contains=cache miss | ✅ GENUINE | cache miss: GENUINE (uses action 内部输出) |

---