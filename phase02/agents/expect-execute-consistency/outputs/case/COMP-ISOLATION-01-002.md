# COMP-ISOLATION-01-002

- 标题: 环境变量不跨 job 泄漏
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- workflow 含两个串行 jobs

操作步骤:
1. job 1 设置环境变量
2. job 2 检查该环境变量

预期结果:
- job 2 不应看到 job 1 设置的环境变量

验证点:
- [负向] job 2 中环境变量值为空或未设置

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Export env | echo "ISOLATION_VAR=leak" >> "$ATOMGIT_ENV" | 是 |
| 2 | Verify env absent | if [ -z "${ISOLATION_VAR:-}" ]; then echo "env not leaked as expected"; else echo "env leaked: $ISOLATION_VAR"; exit 1; fi | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ISOLATION-01-002
dimensions: [completeness, reliability, security]
dimension: completeness
priority: P0
title: 环境变量不跨 job 泄漏
intent_ref: INTENT-COMP-011

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    job1:
      name: Set env
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Export env
          run: |
            echo "ISOLATION_VAR=leak" >> "$ATOMGIT_ENV"
    job2:
      name: Check env
      runs-on: [ubuntu-latest, x64, small]
      needs: job1
      steps:
        - name: Verify env absent
          run: |
            if [ -z "${ISOLATION_VAR:-}" ]; then
              echo "env not leaked as expected"
            else
              echo "env leaked: $ISOLATION_VAR"
              exit 1
            fi

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: run_status
    equals: success
  - type: negative
    target: run_logs
    must_not_contain: env leaked

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
| [负向] job 2 中环境变量值为空或未设置 | ✅ COVERED | negative assertion: must_not_contain "env leaked"；bash 逻辑检查 ISOLATION_VAR 为空 |

### 问题

- 无

---
