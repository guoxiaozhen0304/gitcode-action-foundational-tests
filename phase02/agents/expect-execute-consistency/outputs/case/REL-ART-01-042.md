# REL-ART-01-042

- **标题**: artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-078

通过标准：
1. type=positive, target=upload_outcome, equals=success_or_explicit_rejection_with_limit
2. type=positive, target=md5_match, equals=true_if_upload_success
3. type=negative, target=ghost_artifact_detected, equals=true
4. type=nonfunctional, target=measured_artifact_limit, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate file step | `dd if=/dev/urandom of=big-artifact.bin bs=1M count=2048 md5sum big-artifact.bin ` |  | ✅ GENUINE |
| 2 | upload artifact step | `upload-artifact` |  | ✅ GENUINE |
| 3 | download artifact step | `download-artifact` |  | ✅ GENUINE |
| 4 | verify md5 step | `md5sum big-artifact-2gb` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  upload:
    name: upload 2GB artifact job
    runs-on: [ubuntu-latest, x64, large]
    timeout-minutes: 120
    steps:
      - name: generate file step
        run: |
          dd if=/dev/urandom of=big-artifact.bin bs=1M count=2048
          md5sum big-artifact.bin > expected.md5
      - name: upload artifact step
        uses: upload-artifact
        with:
          name: big-artifact-2gb
          path: big-artifact.bin
  download:
    name: download verify job
    runs-on: [ubuntu-latest, x64, large]
    needs: upload
    timeout-minutes: 120
    steps:
      - name: download artifact step
        uses: download-artifact
        with:
          name: big-artifact-2gb
      - name: verify md5 step
        run: |
          md5sum big-artifact-2gb
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
| 1 | upload_outcome | positive | equals=success_or_explicit_rejection_with_limit | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | md5_match | positive | equals=true_if_upload_success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | ghost_artifact_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | measured_artifact_limit | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---