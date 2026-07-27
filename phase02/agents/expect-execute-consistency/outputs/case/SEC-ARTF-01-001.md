# SEC-ARTF-01-001

- 标题: fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-ARTF-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-019
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行

前置条件:
  - 仓库支持 artifact 上传下载

操作步骤:
  1. 以 fork 贡献者身份提交一个上传 artifact 的 workflow
  2. 在主仓尝试下载该 artifact

预期结果:
  - 主仓不可通过 artifact ID 下载 fork PR 的 artifact
  - 跨仓库 artifact 下载应返回 404 或权限拒绝

验证点:
  - [负向] 主仓 workflow 绝不应能下载到 fork PR 上传的 artifact
  - [非功能] 跨仓库 artifact 下载应返回 404 或权限拒绝，不应静默返回空包

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Create file | run: echo fork content > fork-artifact.txt | 是 |
| 2 | Upload artifact | uses: upload-artifact with name=fork-artifact, path=fork-artifact.txt | 是 |

<details><summary>完整 workflow YAML</summary>

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

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 主仓 workflow 绝不应能下载到 fork PR 上传的 artifact | ✅ COVERED | 步骤真实以 fork 贡献者身份创建文件并上传 artifact（echo 写文件 + uses: upload-artifact），产出了待验证的 artifact |
| [非功能] 跨仓库 artifact 下载应返回 404 或权限拒绝 | ✅ COVERED | 步骤真实上传 artifact 后，断言 target=artifact_download 验证主仓不可下载，步骤为断言提供了真实的前提条件 |

### 问题

无 — 所有验证点均 COVERED。

## 5. 评级理由

两个验证点全部 COVERED：步骤以 fork 贡献者身份真实执行了文件创建（echo fork content > fork-artifact.txt）和 artifact 上传（uses: upload-artifact），为安全隔离断言的验证提供了真实的行为前提。评级为断言一致。
