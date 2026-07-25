# COMP-ENVCTX-01-050

- 标题: env 优先级链 step 大于 job 大于 workflow
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 workflow / job / step 三级定义同名 env 变量
2. 在 step 中输出该变量值验证优先级

预期结果:
- step 级 env 覆盖 job 级，job 级覆盖 workflow 级

验证点:
- [正向] 最终输出值为 step 级定义的值
- [正向] 无 job 级 env 时继承 workflow 级

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Step override | env: MY_VAR=step_value，echo "MY_VAR=$MY_VAR" | 是 |
| 2 | Job inherit | echo "JOB_VAR=$MY_VAR" (无 step 级 env 覆盖) | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ENVCTX-01-050
dimensions: [completeness]
dimension: completeness
priority: P1
title: env 优先级链 step 大于 job 大于 workflow
intent_ref: KEEP-TC-001~004
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
    MY_VAR: workflow_value
  jobs:
    verify:
      name: Verify env priority chain
      runs-on: [ubuntu-latest, x64, small]
      env:
        MY_VAR: job_value
      steps:
        - name: Step override
          env:
            MY_VAR: step_value
          run: |
            echo "MY_VAR=$MY_VAR"
        - name: Job inherit
          run: |
            echo "JOB_VAR=$MY_VAR"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: MY_VAR=step_value
  - type: positive
    target: run_logs
    must_contain: JOB_VAR=job_value
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
| [正向] 最终输出值为 step 级定义的值 | ✅ COVERED | step 级 env MY_VAR=step_value，断言 MY_VAR=step_value |
| [正向] 无 job 级 env 时继承 workflow 级 | ❌ TRIVIAL | 当前 workflow job 级有 env: MY_VAR=job_value，未测试"无 job 级 env"场景；步骤2 JOB_VAR=job_value 验证的是"无 step 级则继承 job 级" |

### 问题

- "无 job 级 env 时继承 workflow 级"未验证：当前 job 级始终有 env 定义，缺失一台 job 无 env 以验证 workflow 级兜底的场景

---
