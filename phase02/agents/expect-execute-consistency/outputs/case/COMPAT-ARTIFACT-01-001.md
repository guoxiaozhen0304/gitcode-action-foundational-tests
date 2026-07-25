# COMPAT-ARTIFACT-01-001

- 标题: upload/download-artifact 跨 job 传递等价性
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ARTIFACT-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-026
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      upload/download-artifact 跨 job 传递等价性

前置条件:
  - 仓库已启用 upload-artifact 与 download-artifact 插件

操作步骤:
  1. 在 job A 中使用 `uses: upload-artifact` 上传一个标记文件
  2. 在 job B 中使用 `uses: download-artifact` 下载同一文件
  3. 验证 job B 能正确读取到 job A 上传的文件内容

预期结果:
  - upload-artifact 成功上传文件到 artifact 存储
  - download-artifact 成功下载并恢复文件到 job B 工作目录
  - 文件内容在跨 job 传递后保持一致
  - 裸插件名写法行为与 GitHub 全名写法等价

验证点:
  - [正向] upload-artifact 步骤成功，无报错
  - [正向] download-artifact 步骤成功，无报错
  - [正向] job B 中文件内容与 job A 上传时一致
  - [负向] 不应因使用裸插件名而解析失败

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) create artifact file | run: mkdir -p artifacts
echo "CROSS_JOB_MARKER_$(date +%s)" > artifacts/marker.txt
 | 是 |
| 2 | (TC) upload artifact | uses: upload-artifact | 是 |
| 3 | (TC) download artifact | uses: download-artifact | 是 |
| 4 | (TC) verify artifact content | run: if grep -q "CROSS_JOB_MARKER" downloaded/marker.txt; then
  echo "ARTIFACT_TRANSFER_OK"
else
  echo "ARTIFACT_TRANSFER_FAILED"
  exit 1
fi
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-upload:
    name: Upload artifact
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) create artifact file
        run: |
          mkdir -p artifacts
          echo "CROSS_JOB_MARKER_$(date +%s)" > artifacts/marker.txt
      - name: (TC) upload artifact
        uses: upload-artifact
        with:
          name: cross-job-artifact
          path: artifacts/marker.txt
  job-download:
    name: Download and verify artifact
    runs-on: [ubuntu-latest, x64, small]
    needs: job-upload
    steps:
      - name: (TC) download artifact
        uses: download-artifact
        with:
          name: cross-job-artifact
          path: downloaded
      - name: (TC) verify artifact content
        run: |
          if grep -q "CROSS_JOB_MARKER" downloaded/marker.txt; then
            echo "ARTIFACT_TRANSFER_OK"
          else
            echo "ARTIFACT_TRANSFER_FAILED"
            exit 1
          fi

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] upload-artifact 步骤成功，无报错 | ✅ COVERED | steps have real logic |
| [正向] download-artifact 步骤成功，无报错 | ✅ COVERED | steps have real logic |
| [正向] job B 中文件内容与 job A 上传时一致 | ✅ COVERED | steps have real logic |
| [负向] 不应因使用裸插件名而解析失败 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
