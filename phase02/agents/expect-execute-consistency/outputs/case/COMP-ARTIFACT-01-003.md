# COMP-ARTIFACT-01-003

- 标题: artifact 保留期设置生效
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- workflow 设置 retention-days: 1

操作步骤:
1. 上传 artifact 并设置 retention-days: 1
2. 等待超过保留期后尝试下载

预期结果:
- 超过保留期后 artifact 不可下载

验证点:
- [正向] 保留期内可下载 artifact
- [负向] 超过保留期后下载返回 404

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Create artifact | echo "temp" > temp.txt | 是 |
| 2 | Upload artifact | uses: upload-artifact with name: temp-artifact, path: temp.txt, retention-days: 1 | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ARTIFACT-01-003
dimensions: [completeness, reliability]
dimension: completeness
priority: P1
title: artifact 保留期设置生效
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
    upload:
      name: Upload with short retention
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Create artifact
          run: |
            echo "temp" > temp.txt
        - name: Upload artifact
          uses: upload-artifact
          with:
            name: temp-artifact
            path: temp.txt
            retention-days: 1

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: artifact_available
    equals: yes_within_retention
  - type: negative
    target: artifact_available_after_expiry
    equals: no_after_1_day

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
| [正向] 保留期内可下载 artifact | ✅ COVERED | 断言 artifact_available=yes_within_retention |
| [负向] 超过保留期后下载返回 404 | ✅ COVERED | negative assertion: artifact_available_after_expiry=no_after_1_day |

### 问题

- 无

---
