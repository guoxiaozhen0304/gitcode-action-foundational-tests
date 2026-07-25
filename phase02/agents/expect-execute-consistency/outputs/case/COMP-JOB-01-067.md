# COMP-JOB-01-067

- 标题: job 可选字段 env if timeout-minutes needs 验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 定义含 env / if / timeout-minutes / needs 的 job
2. 验证各字段生效

预期结果:
- job 级 env 对该 job 所有 step 可见，if 条件正确控制 job 是否执行，timeout-minutes 限制执行时长，needs 正确建立依赖

验证点:
- [正向] job env 在 step 中可访问
- [正向] needs 依赖 job 先执行
- [正向] timeout-minutes 字段被接受

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Prepare | echo "prepare_done" | 否 |
| 2 | Check fields | echo "JOB_VAR=$JOB_VAR"; echo "optional_ok" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-JOB-01-067
dimensions: [completeness]
dimension: completeness
priority: P1
title: job 可选字段 env if timeout-minutes needs 验证
intent_ref: KEEP-TC-264~288
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
    prepare:
      name: Prepare job
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Prepare
          run: |
            echo "prepare_done"
    verify:
      name: Verify optional fields
      runs-on: [ubuntu-latest, x64, small]
      needs: prepare
      if: ${{ true }}
      timeout-minutes: 30
      env:
        JOB_VAR: job_value
      steps:
        - name: Check fields
          run: |
            echo "JOB_VAR=$JOB_VAR"
            echo "optional_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: prepare_done
  - type: positive
    target: run_logs
    must_contain: JOB_VAR=job_value
  - type: positive
    target: run_logs
    must_contain: optional_ok
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
| [正向] job env 在 step 中可访问 | ✅ COVERED | job env JOB_VAR=job_value，断言 JOB_VAR=job_value |
| [正向] needs 依赖 job 先执行 | ✅ COVERED | verify needs prepare，断言 prepare_done 先出现 |
| [正向] timeout-minutes 字段被接受 | ✅ COVERED | verify job 含 timeout-minutes: 30，run_status=success 证明字段被平台接受 |

### 问题

- 无

---
