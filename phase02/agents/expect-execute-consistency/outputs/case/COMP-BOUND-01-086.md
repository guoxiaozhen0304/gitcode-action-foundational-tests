# COMP-BOUND-01-086

- 标题: 矩阵构建 include exclude 与单值边界验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 定义含 matrix include 和 exclude 的 strategy
2. 验证矩阵展开和排除行为

预期结果:
- matrix 支持单变量和多变量，include 添加额外组合，exclude 排除特定组合，单值变量正确展开

验证点:
- [正向] include 添加的组合在 step 中可访问
- [正向] exclude 排除的组合不产生 job 实例
- [正向] 单值变量正确展开

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Matrix value | echo "OS=${{ matrix.os }}"; echo "VER=${{ matrix.version }}"; echo "matrix_ok" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-BOUND-01-086
dimensions: [completeness]
dimension: completeness
priority: P1
title: 矩阵构建 include exclude 与单值边界验证
intent_ref: KEEP-TC-276~328
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
      name: Verify matrix boundary
      runs-on: [ubuntu-latest, x64, small]
      strategy:
        matrix:
          os: [linux]
          version: [1, 2]
          include:
            - os: linux
              version: 3
          exclude:
            - os: linux
              version: 2
      steps:
        - name: Matrix value
          run: |
            echo "OS=${{ matrix.os }}"
            echo "VER=${{ matrix.version }}"
            echo "matrix_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: matrix_ok
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
| [正向] include 添加的组合在 step 中可访问 | ✅ COVERED | 矩阵有 [1, 2, 3] 三值（含 include 的 version: 3），matrix_ok 断言覆盖所有成功实例 |
| [正向] exclude 排除的组合不产生 job 实例 | ❌ UNVERIFIABLE | 单次 dispatch 无法证明 version=2 的组合未产生实例 |
| [正向] 单值变量正确展开 | ✅ COVERED | os: [linux] 单值，矩阵执行成功证明正确展开 |

### 问题

- exclude 排除验证不可达：需要统计 job 实例数量证明 version=2 未执行，但当前无此类断言

---
