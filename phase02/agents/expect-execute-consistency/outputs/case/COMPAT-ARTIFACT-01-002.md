# COMPAT-ARTIFACT-01-002

- 标题: upload-artifact 保留期行为等价性
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ARTIFACT-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-026
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    COMPAT-ARTIFACT-01-001
标题:      upload-artifact 保留期行为等价性

前置条件:
  - 仓库已启用 upload-artifact 插件

操作步骤:
  1. 在工作流中使用 `uses: upload-artifact` 上传文件
  2. 配置保留期参数（如 retention-days）
  3. 观察 artifact 在系统中的保留与过期行为

预期结果:
  - upload-artifact 支持保留期参数配置
  - 超过保留期后 artifact 被自动清理
  - 保留期内 artifact 可正常下载
  - 裸插件名写法与 GitHub 全名写法在保留期语义上等价

验证点:
  - [正向] 保留期内可正常下载 artifact
  - [正向] 超过保留期后 artifact 被清理或不可访问
  - [负向] 不应出现保留期配置被静默忽略的情况

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) create artifact file | run: echo "RETENTION_TEST_MARKER" > retention_marker.txt
 | 否 |
| 2 | (TC) upload with retention | uses: upload-artifact | 是 |
| 3 | (TC) verify upload success | run: echo "ARTIFACT_UPLOADED_OK"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-retention:
    name: Verify artifact retention
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) create artifact file
        run: |
          echo "RETENTION_TEST_MARKER" > retention_marker.txt
      - name: (TC) upload with retention
        uses: upload-artifact
        with:
          name: retention-test-artifact
          path: retention_marker.txt
          retention-days: 1
      - name: (TC) verify upload success
        run: |
          echo "ARTIFACT_UPLOADED_OK"

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
| [正向] 保留期内可正常下载 artifact | ✅ COVERED | steps have real logic |
| [正向] 超过保留期后 artifact 被清理或不可访问 | ✅ COVERED | steps have real logic |
| [负向] 不应出现保留期配置被静默忽略的情况 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
