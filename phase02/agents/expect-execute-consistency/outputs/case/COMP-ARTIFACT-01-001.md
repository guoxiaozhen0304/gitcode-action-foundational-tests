# COMP-ARTIFACT-01-001

- 标题: artifact 可在同 workflow 的 job 间正确传递
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- workflow 含 upload-artifact 和 download-artifact

操作步骤:
1. job 1 生成文件并 upload-artifact
2. job 2 通过 needs 依赖下载 artifact
3. 验证文件内容一致性

预期结果:
- job 2 下载的 artifact 内容与 job 1 上传的一致

验证点:
- [正向] download 后文件内容正确
- [正向] 运行状态成功

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Create artifact | mkdir -p dist; echo "hello artifact" > dist/app.txt | 是 |
| 2 | Upload artifact | uses: upload-artifact with name: app-dist, path: dist/ | 是 |
| 3 | Download artifact | uses: download-artifact with name: app-dist, path: dist/ | 是 |
| 4 | Verify content | cat dist/app.txt | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ARTIFACT-01-001
dimensions: [completeness, reliability]
dimension: completeness
priority: P1
title: artifact 可在同 workflow 的 job 间正确传递
intent_ref: INTENT-COMP-015

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    build:
      name: Build and upload
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Create artifact
          run: |
            mkdir -p dist
            echo "hello artifact" > dist/app.txt
        - name: Upload artifact
          uses: upload-artifact
          with:
            name: app-dist
            path: dist/
    verify:
      name: Download and verify
      runs-on: [ubuntu-latest, x64, small]
      needs: build
      steps:
        - name: Download artifact
          uses: download-artifact
          with:
            name: app-dist
            path: dist/
        - name: Verify content
          run: |
            cat dist/app.txt

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: run_status
    equals: success
  - type: positive
    target: run_logs
    contains: hello artifact

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] download 后文件内容正确 | ✅ COVERED | 步骤4 cat dist/app.txt 输出"hello artifact"，断言 run_logs contains "hello artifact" |
| [正向] 运行状态成功 | ✅ COVERED | 断言 run_status=success |

### 问题

- 无

---
