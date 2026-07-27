# USE-RES-01-001

- 标题: runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名
- 维度: usability | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - 文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 对 runtime-environment-variables.md 全文进行字符串扫描

预期结果:
  独立出现的环境变量示例均使用 ATOMGIT_ 前缀；未标注为 GitHub 对照的 GITHUB_ 残留数量为 0

验证点:
  - [正向] 所有独立环境变量示例使用 ATOMGIT_ 前缀
  - [负向] 正文中不应出现未标注为 GitHub 对照的 GITHUB_ACTION_PATH、GITHUB_ENV 等残留措辞

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-RES-01-001
dimensions: ["usability"]
dimension: usability
priority: P1
title: "runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名"
intent_ref: INTENT-USE-012

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
  - type: negative
    target: documentation
    eval: llm_assisted
    rubric: "独立出现的 GITHUB_ 前缀（非引用、非对照表场景）数量应为 0"

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
| [正向] 所有独立环境变量示例使用 ATOMGIT_ 前缀 | ❌ MISSING | workflow=null，无步骤扫描文档进行字符串匹配 |
| [负向] 正文无未标注 GITHUB_ 残留措辞 | ❌ MISSING | workflow=null，无步骤执行文档字符串扫描；YAML 有 type=negative 但 eval=llm_assisted 无步骤支撑 |

### 问题

- [正向] ATOMGIT_ 前缀: MISSING — workflow=null, no steps to scan/document-review
- [负向] GITHUB_ 残留: MISSING — workflow=null, no steps to perform string scanning; assertion is llm_assisted

---
