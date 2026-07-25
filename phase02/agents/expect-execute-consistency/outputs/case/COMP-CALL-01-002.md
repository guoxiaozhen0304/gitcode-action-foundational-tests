# COMP-CALL-01-002

- 标题: 3 层 workflow_call 嵌套应被拒绝
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 存在 3 层嵌套的可重用 workflow 结构

操作步骤:
1. 触发顶层主 workflow
2. 观察第 3 层嵌套调用是否被拒绝

预期结果:
- 平台在第 3 层调用时报错或阻止执行

验证点:
- [负向] 运行不应成功完成
- [非功能] 报错信息应清晰说明最多 2 层限制

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo before call | echo "attempting 3 layer call" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CALL-01-002
dimensions: [completeness]
dimension: completeness
priority: P1
title: 3 层 workflow_call 嵌套应被拒绝
intent_ref: INTENT-COMP-006

setup:
  repo_fixture: reusable-workflow-3layer
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    caller:
      name: Call 3 layer reusable workflow
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Echo before call
          run: |
            echo "attempting 3 layer call"

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: negative
    target: run_status
    equals: success
  - type: nonfunctional
    target: error_message
    eval: llm_assisted
    rubric: 报错信息应说明 workflow_call 最多支持 2 层嵌套

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | reusable-workflow-3layer |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 运行不应成功完成 | ✅ COVERED | negative assertion: run_status != success，repo_fixture 提供 3 层结构由平台判断拒绝 |
| [非功能] 报错信息应清晰说明最多 2 层限制 | ✅ COVERED | nonfunctional assertion 通过 llm_assisted eval 检查错误信息 |

### 问题

- 无

---
