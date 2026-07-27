# REL-FAULT-01-035

- **标题**: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-035

通过标准：
1. type=positive, target=step_status, equals=failure
2. type=positive, target=run_logs, contains="503"
3. type=positive, target=job_status, equals=failure

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | download artifact step | `download-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: fault injection artifact 503
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: download artifact step
        uses: download-artifact
        with:
          name: missing-artifact
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'concurrent_flood', 'params': {'service': 'artifact_download', 'response': 503, 'target_step': 1}, 'recovery_expectation': 'explicit_error_and_rerun_success'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals=failure | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_logs | positive | contains=503 | ✅ GENUINE | 503: GENUINE (uses action 内部输出) |
| 3 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |

---