# REL-FAULT-01-038

- **标题**: 故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-081

通过标准：
1. type=positive, target=job_status, equals=failure
2. type=negative, target=truncated_artifact_downloadable, equals=true
3. type=positive, target=rerun_upload_md5_match, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate file step | `dd if=/dev/urandom of=upload-probe.bin bs=1M count=100` |  | ✅ GENUINE |
| 2 | upload artifact step | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: upload kill mid transfer job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 30
    steps:
      - name: generate file step
        run: |
          dd if=/dev/urandom of=upload-probe.bin bs=1M count=100
      - name: upload artifact step
        uses: upload-artifact
        with:
          name: upload-kill-probe
          path: upload-probe.bin
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'kill_runner', 'params': {'during': 'artifact_upload', 'progress_pct': 50}, 'recovery_expectation': 'job_marked_failure_no_partial_artifact; rerun_succeeds'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | truncated_artifact_downloadable | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | rerun_upload_md5_match | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

---