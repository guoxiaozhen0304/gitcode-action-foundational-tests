# USE-PATH-01-001

- 标题: paths 300 文件上限在文档与行为中一致且明示
- 维度: usability/compatibility | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - 文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 检查 configure-triggers.md 中 paths 说明
  2. 触发一次变更文件数超过 300 的 push

预期结果:
  文档在显眼位置标注 300 文件上限；超出时调试日志有提示

验证点:
  - [非功能] 文档 paths 章节顶部或注意块中是否有 300 文件上限提示
  - [非功能] 超出上限时调试日志是否提示 paths 过滤超出文件上限

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-PATH-01-001
dimensions: ["usability", "compatibility"]
dimension: usability
priority: P1
title: "paths 300 文件上限在文档与行为中一致且明示"
intent_ref: INTENT-USE-015

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
    rubric: "文档 configure-triggers.md 中 paths/paths-ignore 说明必须在首段或独立的注意块中写明匹配前 300 个变更文件"

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
| [非功能] 文档 paths 章节有 300 文件上限提示 | ❌ MISSING | workflow=null，无步骤审查文档内容 |
| [非功能] 超出上限时调试日志提示 | ❌ MISSING | workflow=null，无步骤触发 >300 文件变更 push；断言 eval=llm_assisted |

### 问题

- [非功能] 文档 300 上限提示: MISSING — workflow=null, no steps to verify documentation content
- [非功能] 调试日志提示: MISSING — workflow=null, no steps to exercise >300 file push scenario; assertion is llm_assisted

---
