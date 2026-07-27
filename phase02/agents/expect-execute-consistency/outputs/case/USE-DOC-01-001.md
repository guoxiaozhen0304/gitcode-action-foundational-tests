# USE-DOC-01-001

- 标题: stages 与 post 概念在迁移文档中具备可发现性
- 维度: usability | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - 文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 在文档首页/快速入门/迁移指引中搜索 stages 与 post 关键词

预期结果:
  相关说明出现在显眼位置（首屏或前 3 个可见章节内），并给出与 GitHub 的差异标注

验证点:
  - [正向] 迁移相关页面有 stages/post 的入口链接
  - [非功能] 说明是否包含 GitCode 特有/GitHub 无此概念等显式差异标注

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-DOC-01-001
dimensions: ["usability"]
dimension: usability
priority: P1
title: "stages 与 post 概念在迁移文档中具备可发现性"
intent_ref: INTENT-USE-011

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: null

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: nonfunctional
    target: documentation
    eval: llm_assisted
    rubric: "文档中关于 stages/post 的说明必须在迁移相关或快速入门类页面中有入口链接，且说明包含 GitCode 特有/GitHub 无此概念等显式差异标注"

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
| [正向] 迁移相关页面有 stages/post 的入口链接 | ❌ MISSING | workflow=null，无步骤产出文档内容验证 |
| [非功能] 说明包含 GitCode 特有差异标注 | ❌ MISSING | workflow=null，无步骤能进行文档审查；断言 eval=llm_assisted |

### 问题

- [正向] 迁移相关页面有 stages/post 入口链接: MISSING — workflow=null, no steps to verify documentation
- [非功能] 差异标注: MISSING — workflow=null, no steps to evaluate documentation content; assertion is llm_assisted

---
