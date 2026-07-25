# COMP-ARTIFACT-01-002

- 标题: 下载全部制品功能正常
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- workflow 上传多个 artifacts

操作步骤:
1. job 1 上传多个 artifacts
2. job 2 不指定 name 下载全部 artifacts

预期结果:
- 所有 artifacts 被下载到指定目录

验证点:
- [正向] 所有 artifact 文件均存在

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Create artifacts | mkdir -p dist reports; echo "app" > dist/app.txt; echo "report" > reports/coverage.txt | 是 |
| 2 | Upload app | uses: upload-artifact with name: app, path: dist/ | 是 |
| 3 | Upload reports | uses: upload-artifact with name: reports, path: reports/ | 是 |
| 4 | Download all | uses: download-artifact with path: artifacts/ (no name) | 是 |
| 5 | Verify all | cat artifacts/app/app.txt; cat artifacts/reports/coverage.txt | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ARTIFACT-01-002
dimensions: [completeness, reliability]
dimension: completeness
priority: P1
title: 下载全部制品功能正常
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
      name: Build multiple artifacts
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Create artifacts
          run: |
            mkdir -p dist reports
            echo "app" > dist/app.txt
            echo "report" > reports/coverage.txt
        - name: Upload app
          uses: upload-artifact
          with:
            name: app
            path: dist/
        - name: Upload reports
          uses: upload-artifact
          with:
            name: reports
            path: reports/
    verify:
      name: Download all artifacts
      runs-on: [ubuntu-latest, x64, small]
      needs: build
      steps:
        - name: Download all
          uses: download-artifact
          with:
            path: artifacts/
        - name: Verify all
          run: |
            cat artifacts/app/app.txt
            cat artifacts/reports/coverage.txt

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
    contains: app
  - type: positive
    target: run_logs
    contains: report

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
| [正向] 所有 artifact 文件均存在 | ✅ COVERED | 步骤5 cat 两个文件，断言 run_logs contains "app" 和 "report" |

### 问题

- 无

---
