# USE-DIR-01-002

- 标题: .github/workflows/ 下 workflow 未被识别时应给出目录差异提示
- 维度: usability | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - 仓库同时存在 .github/workflows/ 和 .gitcode/workflows/
  - 前者含 workflow 后者为空

操作步骤:
  1. 将 workflow 文件误放到 .github/workflows/ 目录
  2. 推送代码触发 push 事件

预期结果:
  系统在某处（运行页面、日志或校验信息）提示 .gitcode/workflows/ 为正确目录，而非静默忽略

验证点:
  - [负向] 不应无任何提示地忽略 .github/workflows/ 下的文件
  - [非功能] 提示信息中应包含 .gitcode/workflows 字样

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-DIR-01-002
dimensions: ["usability"]
dimension: usability
priority: P1
title: ".github/workflows/ 下 workflow 未被识别时应给出目录差异提示"
intent_ref: INTENT-USE-001

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
    target: system_message
    eval: llm_assisted
    rubric: "提示信息必须同时包含 .github/workflows 与 .gitcode/workflows 对照字样，并指明 GitCode 使用 .gitcode/workflows 目录存放工作流文件"

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
| [负向] 不应无任何提示地忽略 .github/workflows/ 下的文件 | ❌ UNVERIFIABLE | workflow=null，无步骤产出；single dispatch cannot prove negation |
| [非功能] 提示信息中应包含 .gitcode/workflows 字样 | ❌ MISSING | workflow=null，无步骤能产生 system_message；断言 eval=llm_assisted |

### 问题

- [负向] 不应无任何提示地忽略: UNVERIFIABLE — workflow=null, no steps, single dispatch cannot prove negation
- [非功能] 提示信息应包含 .gitcode/workflows: MISSING — workflow=null, no steps could produce system messages; assertion is llm_assisted

---
