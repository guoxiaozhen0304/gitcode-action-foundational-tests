# COMP-CTX-01-051

- 标题: 上下文在 workflow job step 各级注入验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 workflow 级 env 中引用 atomgit 上下文
2. 在 job 级 env 中引用 env 上下文
3. 在 step 级 run 中引用 job 上下文和 atomgit 上下文

预期结果:
- atomgit / env / job 上下文在各级均可正常解析并注入

验证点:
- [正向] workflow 级 env 可解析 atomgit 属性
- [正向] job 级 env 可解析 env 属性
- [正向] step 级 run 可解析 job 和 atomgit 属性

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Step context | echo "WF_REF=$WF_REF"; echo "JOB_REF=$JOB_REF"; echo "JOB_STATUS=${{ job.status }}"; echo "ATOMGIT_REF=${{ atomgit.ref }}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CTX-01-051
dimensions: [completeness]
dimension: completeness
priority: P1
title: 上下文在 workflow job step 各级注入验证
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
  env:
    WF_REF: ${{ atomgit.ref }}
  jobs:
    verify:
      name: Verify context injection at all levels
      runs-on: [ubuntu-latest, x64, small]
      env:
        JOB_REF: ${{ env.WF_REF }}
      steps:
        - name: Step context
          run: |
            echo "WF_REF=$WF_REF"
            echo "JOB_REF=$JOB_REF"
            echo "JOB_STATUS=${{ job.status }}"
            echo "ATOMGIT_REF=${{ atomgit.ref }}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: WF_REF=refs/
  - type: positive
    target: run_logs
    must_contain: JOB_REF=refs/
  - type: positive
    target: run_logs
    must_contain: JOB_STATUS=
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
| [正向] workflow 级 env 可解析 atomgit 属性 | ✅ COVERED | workflow env WF_REF=${{ atomgit.ref }}，输出 WF_REF=refs/ |
| [正向] job 级 env 可解析 env 属性 | ✅ COVERED | job env JOB_REF=${{ env.WF_REF }}，输出 JOB_REF=refs/ |
| [正向] step 级 run 可解析 job 和 atomgit 属性 | ✅ COVERED | step 内 ${{ job.status }} 和 ${{ atomgit.ref }} 均输出有效值 |

### 问题

- 无

---
