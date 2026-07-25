# COMP-JOB-01-068

- 标题: job strategy 矩阵与 continue-on-error 验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 定义含 strategy.matrix 和 continue-on-error 的 job
2. 验证矩阵展开和容错行为

预期结果:
- strategy.matrix 正确展开多实例，continue-on-error true 时 job 失败不终止 workflow

验证点:
- [正向] 矩阵变量在 step 中可访问
- [正向] continue-on-error true 被接受
- [正向] fail-fast 字段被接受

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Matrix value | echo "VERSION=${{ matrix.version }}"; echo "strategy_ok" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-JOB-01-068
dimensions: [completeness]
dimension: completeness
priority: P1
title: job strategy 矩阵与 continue-on-error 验证
intent_ref: KEEP-TC-276~278
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
      name: Verify strategy and matrix
      runs-on: [ubuntu-latest, x64, small]
      strategy:
        matrix:
          version: [a, b]
        fail-fast: false
      continue-on-error: true
      steps:
        - name: Matrix value
          run: |
            echo "VERSION=${{ matrix.version }}"
            echo "strategy_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: VERSION=a
  - type: positive
    target: run_logs
    must_contain: VERSION=b
  - type: positive
    target: run_logs
    must_contain: strategy_ok
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
| [正向] 矩阵变量在 step 中可访问 | ✅ COVERED | 断言 VERSION=a 和 VERSION=b，证明矩阵展开为两个实例 |
| [正向] continue-on-error true 被接受 | ✅ COVERED | continue-on-error: true，run_status=success 证明平台接受该字段 |
| [正向] fail-fast 字段被接受 | ✅ COVERED | fail-fast: false，run_status=success 证明平台接受该字段 |

### 问题

- 无

---
