# REL-FAULT-01-033

- **标题**: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-033

通过标准：
1. type=positive, target=job_status, equals=failure
2. type=positive, target=run_logs, contains="No space left on device"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | prefill disk | `fallocate -l 49.5G prefill.bin || dd if=/dev/zero of=prefill.bin bs=1M count=506` |  | ✅ GENUINE |
| 2 | write additional 2GB | `dd if=/dev/zero of=extra.bin bs=1M count=2048` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: fault injection disk full
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: prefill disk
        run: |
          fallocate -l 49.5G prefill.bin || dd if=/dev/zero of=prefill.bin bs=1M count=50688
      - name: write additional 2GB
        run: |
          dd if=/dev/zero of=extra.bin bs=1M count=2048
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'pre_job', 'action': 'disk_full', 'params': {'pre_fill_gb': 49.5, 'append_gb': 2}, 'recovery_expectation': 'explicit_error_and_user_retry'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | run_logs | positive | contains=No space left on device | ❌ MISSING_SOURCE | No space left on device: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 2 — MISSING_SOURCE**❌: No space left on device: MISSING_SOURCE (无步骤产出此字符串)

---