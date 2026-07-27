# USE-VARS-01-001

- 标题: vars 上下文在文档与样本中的声明必须一致
- 维度: usability | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - 文档与样本版本为 2026-07-20 抓取版本

操作步骤:
  1. 比对 syntax-reference/context.md 与 workflow-samples 注释对 vars 的支持声明

预期结果:
  两者声明一致：要么均支持，要么均不支持

验证点:
  - [正向] 若支持，文档示例可运行且样本注释已移除已知不支持
  - [负向] 若不支持，文档中不应出现 vars 使用示例

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-VARS-01-001
dimensions: ["usability"]
dimension: usability
priority: P1
title: "vars 上下文在文档与样本中的声明必须一致"
intent_ref: INTENT-USE-014

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
    rubric: "文档与样本对同一能力 vars 上下文的声明必须一致；不一致即视为可理解性缺陷"

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
| [正向] 若支持，文档示例可运行且样本注释已移除 | ❌ MISSING | workflow=null，无步骤能够运行文档示例或检查样本注释 |
| [负向] 若不支持，文档中不应出现 vars 使用示例 | ❌ MISSING | workflow=null，无步骤进行文档/样本对比；assertion eval=llm_assisted |

### 问题

- [正向] 文档示例/样本验证: MISSING — workflow=null, no steps to run document examples or inspect sample annotations
- [负向] 文档无 vars 示例: MISSING — workflow=null, no steps to perform doc cross-referencing; assertion is llm_assisted

---
