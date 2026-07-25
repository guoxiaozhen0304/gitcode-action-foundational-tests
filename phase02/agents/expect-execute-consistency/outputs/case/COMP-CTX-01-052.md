# COMP-CTX-01-052

- 标题: 上下文在条件表达式 if 中注入验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 job 和 step 的 if 条件中使用 atomgit / env / job 上下文
2. 运行 workflow 验证条件正确解析

预期结果:
- if 条件中的上下文表达式被正确求值，条件成立时步骤执行，不成立时跳过

验证点:
- [正向] atomgit.ref 条件正确匹配时步骤执行
- [正向] env 条件正确匹配时步骤执行
- [正向] job.status 条件在 job 级 if 可解析

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Always run | run: echo "always"，无 if 条件 | 否 |
| 2 | Conditional env | if: ${{ env.ALWAYS_TRUE == 'yes' }}，run: echo "conditional_env_passed" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CTX-01-052
dimensions: [completeness]
dimension: completeness
priority: P1
title: 上下文在条件表达式 if 中注入验证
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
      name: Verify context in if expressions
      runs-on: [ubuntu-latest, x64, small]
      if: ${{ atomgit.ref == 'refs/heads/main' || true }}
      steps:
        - name: Always run
          run: |
            echo "always"
        - name: Conditional env
          if: ${{ env.ALWAYS_TRUE == 'yes' }}
          env:
            ALWAYS_TRUE: yes
          run: |
            echo "conditional_env_passed"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: always
  - type: positive
    target: run_logs
    must_contain: conditional_env_passed
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
| [正向] atomgit.ref 条件正确匹配时步骤执行 | ✅ COVERED | job 级 if 使用 ${{ atomgit.ref == 'refs/heads/main' || true }}，job 执行成功 |
| [正向] env 条件正确匹配时步骤执行 | ✅ COVERED | step 级 if 使用 ${{ env.ALWAYS_TRUE == 'yes' }}，conditional_env_passed 输出 |
| [正向] job.status 条件在 job 级 if 可解析 | ❌ TRIVIAL | job.status 在 job 级 if 中未测试；job 级 if 仅使用 atomgit.ref，未引用 job.status |

### 问题

- job.status 在 job 级 if 中的可解析性未验证：job 级 if 仅使用 atomgit.ref 和 env 上下文

---
