# REL-ARTPERF-01-053-V2

- **标题**: 制品传输性能——1GB artifact 上传下载耗时
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**制品传输性能——1GB artifact 上传下载耗时**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-053

通过标准：
1. type=nonfunctional, target=upload_time_seconds
2. type=nonfunctional, target=download_time_seconds
3. type=positive, target=hash_match, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate 1024MB file | `dd if=/dev/urandom of=artifact.bin bs=1M count=1024` |  | ✅ GENUINE |
| 2 | upload artifact step | `upload-artifact` |  | ✅ GENUINE |
| 3 | download artifact step | `download-artifact` |  | ✅ GENUINE |
| 4 | verify artifact step | `ls -la perf-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  upload:
    name: upload artifact job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: generate 1024MB file
        run: |
          dd if=/dev/urandom of=artifact.bin bs=1M count=1024
      - name: upload artifact step
        uses: upload-artifact
        with:
          name: perf-artifact
          path: artifact.bin
  download:
    name: download artifact job
    runs-on: [ubuntu-latest, x64, small]
    needs: upload
    steps:
      - name: download artifact step
        uses: download-artifact
        with:
          name: perf-artifact
      - name: verify artifact step
        run: |
          ls -la perf-artifact
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
| 1 | upload_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | download_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | hash_match | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---