# REL-FAULT-01-032

- **标题**: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-032

通过标准：
1. type=positive, target=step_status, equals=failure
2. type=positive, target=run_logs, contains="network"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate artifact file | `dd if=/dev/urandom of=artifact.bin bs=1M count=10` |  | ✅ GENUINE |
| 2 | upload artifact step | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: fault injection network partition
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: generate artifact file
        run: |
          dd if=/dev/urandom of=artifact.bin bs=1M count=10
      - name: upload artifact step
        uses: upload-artifact
        with:
          name: net-fault-artifact
          path: artifact.bin
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'network_partition', 'params': {'duration_seconds': 30, 'target_step': 2}, 'recovery_expectation': 'explicit_error_and_rerun_success'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | equals=failure | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_logs | positive | contains=network | ✅ GENUINE | network: GENUINE (uses action 内部输出) |

---