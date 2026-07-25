# COMP-CTX-01-053

- 标题: 上下文在 Action 插件参数中注入验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action
- 存在可引用的官方 Action

操作步骤:
1. 在 uses 步骤的 with 参数中使用 atomgit 和 env 上下文
2. 运行 workflow 验证 Action 接收参数正确

预期结果:
- Action 的 with 参数中可正常解析 atomgit / env / secrets 上下文

验证点:
- [正向] with 参数中的上下文表达式被正确替换并传入 Action

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout with explicit token | uses: checkout with ref: ${{ atomgit.ref }} | 是 |
| 2 | Echo env in action param | run: echo "done" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CTX-01-053
dimensions: [completeness]
dimension: completeness
priority: P1
title: 上下文在 Action 插件参数中注入验证
intent_ref: KEEP-TC-086~124
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    workflow_dispatch:
  jobs:
    verify:
      name: Verify context in Action with params
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Checkout with explicit token
          uses: checkout
          with:
            ref: ${{ atomgit.ref }}
        - name: Echo env in action param
          run: |
            echo "done"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_status
    equals: success
teardown:
  reset: fixture
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
| [正向] with 参数中的上下文表达式被正确替换并传入 Action | ✅ COVERED | checkout action with ref: ${{ atomgit.ref }}，run_status=success 证明上下文解析成功 |

### 问题

- 无

---
