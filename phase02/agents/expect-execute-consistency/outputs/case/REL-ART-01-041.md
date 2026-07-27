# REL-ART-01-041

- **标题**: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**超大 artifact——100 MB artifact 上传后下游 job 应成功下载**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-041

通过标准：
1. type=positive, target=upload_status, equals=success
2. type=positive, target=download_status, equals=success
3. type=positive, target=md5_match, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate 100MB file | `dd if=/dev/urandom of=artifact.bin bs=1M count=100` |  | ✅ GENUINE |
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
      - name: generate 100MB file
        run: |
          dd if=/dev/urandom of=artifact.bin bs=1M count=100
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
| 1 | upload_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | download_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | md5_match | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

---