# COMP-CALL-01-001

- 标题: 2 层 workflow_call 嵌套正常执行
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 存在可重用的子 workflow（1 层）
- 主 workflow 调用子 workflow（2 层总计）

操作步骤:
1. 触发主 workflow
2. 观察嵌套调用是否成功完成

预期结果:
- 2 层嵌套 workflow_call 成功执行
- 子 workflow 的输出正确传递回主 workflow

验证点:
- [正向] 运行状态成功
- [正向] 子 workflow 的 step 日志可见

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo before call | echo "calling reusable workflow" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CALL-01-001
dimensions: [completeness]
dimension: completeness
priority: P1
title: 2 层 workflow_call 嵌套正常执行
intent_ref: INTENT-COMP-006

setup:
  repo_fixture: reusable-workflow
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    caller:
      name: Call reusable workflow
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Echo before call
          run: |
            echo "calling reusable workflow"

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: run_status
    equals: success

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | reusable-workflow |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 运行状态成功 | ✅ COVERED | 断言 run_status=success，但成功仅证明 echo 步骤执行 |
| [正向] 子 workflow 的 step 日志可见 | ❌ TRIVIAL | 当前 workflow 仅含一个 echo 步骤，未通过 `uses:` 调用子 workflow；子 workflow 的执行依赖 repo_fixture 提供结构但无显式调用 |

### 问题

- 当前 workflow 内容仅 echo，未显式 `uses:<reusable-workflow>` 调用子 workflow；子 workflow 步骤日志可见性依赖 fixture 隐式执行，workflow 自身无验证该行为

---
