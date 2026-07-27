# USE-UNKN-01-001

- 标题: 未知字段如 run-name 不应被静默忽略而应给出警告或错误
- 维度: usability/compatibility | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 中使用 GitHub 特有的 run-name 字段

预期结果:
  系统在校验阶段给出警告或错误，指明字段不支持

验证点:
  - [负向] 不应静默忽略未知字段
  - [非功能] 报错中是否包含字段名、文件路径、不支持字样

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | step | `echo "hello"` | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-UNKN-01-001
dimensions: ["usability", "compatibility"]
dimension: usability
priority: P1
title: "未知字段如 run-name 不应被静默忽略而应给出警告或错误"
intent_ref: INTENT-USE-023

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  run-name: Build by ${{ atomgit.actor }}
  name: unknown field test
  on:
    workflow_dispatch:
  jobs:
    bad:
      name: unknown field run-name
      runs-on: [ubuntu-latest, x64, small]
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
    rubric: "对未知字段的提示必须包含字段名和不支持/unknown 字样；若能识别该字段为 GitHub 特有如 run-name，提示中应追加该字段为 GitHub Actions 特有，GitCode 暂不支持"

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
| [负向] 不应静默忽略未知字段 | ❌ UNVERIFIABLE | workflow 含 `run-name: Build by ${{ atomgit.actor }}` 字段可触发平台解析，但 single dispatch cannot prove negation of silent ignore |
| [非功能] 报错包含字段名、路径、不支持字样 | ❌ TRIVIAL | 步骤仅 `echo "hello"`，无 if:/${{ }}/uses:/实质命令；步骤不产生平台级校验报错；断言 eval=llm_assisted |

### 问题

- [负向] 不应静默忽略: UNVERIFIABLE — workflow 含 `run-name` + `${{ atomgit.actor }}` 可触发解析行为，但单次运行无法证明平台不会静默忽略
- [非功能] 报错内容: TRIVIAL — 唯一步骤仅 echo "hello"，不产生平台校验警告；断言依赖 LLM 评估 runner 日志

---
