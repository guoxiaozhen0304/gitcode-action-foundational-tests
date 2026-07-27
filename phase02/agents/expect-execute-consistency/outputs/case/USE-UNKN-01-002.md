# USE-UNKN-01-002

- 标题: 未知字段报错若识别为 GitHub 特有应追加迁移提示
- 维度: usability/compatibility | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 中使用 GitHub 特有的 jobs.<id>.container 字段

预期结果:
  报错除指出字段不支持外，还提示该字段为 GitHub Actions 特有

验证点:
  - [非功能] 报错中是否出现 GitHub Actions 特有等迁移提示

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | step | `echo "hello"` | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-UNKN-01-002
dimensions: ["usability", "compatibility"]
dimension: usability
priority: P1
title: "未知字段报错若识别为 GitHub 特有应追加迁移提示"
intent_ref: INTENT-USE-023

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    bad:
      name: github specific field container
      runs-on: [ubuntu-latest, x64, small]
      container:
        image: node:20
      steps:
        - name: step
          run: |
            echo "hello"

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: nonfunctional
    target: error_message
    eval: llm_assisted
    rubric: "对未知字段的提示必须包含字段名和不支持/unknown 字样；若能识别该字段为 GitHub 特有如 container，提示中应追加该字段为 GitHub Actions 特有，GitCode 暂不支持"

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
| [非功能] 报错中出现 GitHub Actions 特有迁移提示 | ❌ TRIVIAL | 步骤仅 `echo "hello"`，无 if:/${{ }}/uses:/实质命令；步骤不产生平台级校验报错；断言 eval=llm_assisted |

### 问题

- [非功能] 迁移提示: TRIVIAL — workflow 含 `container: image: node:20` 字段可触发平台解析，但唯一步骤仅 echo "hello"，不产生校验警告；断言依赖 LLM 评估 runner 日志

---
