# SEC-ARTF-01-001

- **标题**: fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-019

通过标准：
1. type=negative, target=artifact_download
2. type=positive, target=artifact_download, equals=404_or_permission_denied

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create file | `echo fork content > fork-artifact.txt` |  | ❌ VACUOUS |
| 2 | Upload artifact | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  artifact-upload:
    name: Upload artifact from fork
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create file
        run: |
          echo fork content > fork-artifact.txt
      - name: Upload artifact
        uses: upload-artifact
        with:
          name: fork-artifact
          path: fork-artifact.txt
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-artifacts` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_download | negative |  | ✅ GENUINE | 通用断言匹配 |
| 2 | artifact_download | positive | equals=404_or_permission_denied | ✅ GENUINE | 断言有条件可被步骤验证 |

---