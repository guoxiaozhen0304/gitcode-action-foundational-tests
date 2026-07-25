# COMP-JOB-01-066

- 标题: job 必填字段 name runs-on steps 验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 定义含 name / runs-on / steps 的 job
2. 验证缺任一字段时平台拒绝

预期结果:
- job 必须包含 name / runs-on / steps，缺 name 时报空值错误，缺 runs-on 或 steps 时平台拒绝

验证点:
- [正向] 完整 job 定义通过校验并执行
- [负向] 缺 name 被平台拒绝
- [负向] 缺 steps 被平台拒绝

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | echo "job_fields_ok" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-JOB-01-066
dimensions: [completeness]
dimension: completeness
priority: P1
title: job 必填字段 name runs-on steps 验证
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
    verify:
      name: Verify required job fields
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Echo ok
          run: |
            echo "job_fields_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_status
    equals: success
  - type: positive
    target: run_logs
    must_contain: job_fields_ok
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
| [正向] 完整 job 定义通过校验并执行 | ✅ COVERED | job 含 name+runs-on+steps，run_status=success |
| [负向] 缺 name 被平台拒绝 | ❌ UNVERIFIABLE | 仅测试合法 job，未提交缺 name 的 workflow 验证拒绝行为 |
| [负向] 缺 steps 被平台拒绝 | ❌ UNVERIFIABLE | 同上，缺 steps 的 neg case 未实现 |

### 问题

- 负向验证点全部缺失：仅验证合法 job 通过，未创建缺 name/steps 的 workflow 变体测试拒绝行为

---
