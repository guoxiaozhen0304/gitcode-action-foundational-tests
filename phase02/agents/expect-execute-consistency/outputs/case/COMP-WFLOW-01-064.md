# COMP-WFLOW-01-064

- 标题: workflow stages 阶段结构字段验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-WFLOW-01-064
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-366~401
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow stages 阶段结构字段验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 stages 的 workflow，使用 map 格式
  2. 验证 stage 间串行和 fail_fast

预期结果:
  - stages 为 map 格式，每个 stage 含 jobs，stage 间串行执行，fail_fast 控制失败时是否中断

验证点:
  - [正向] stages map 格式通过校验
  - [正向] 单 stage 可缺省 stages 字段
  - [正向] fail_fast true 时某 job 失败中断后续 stage

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (no steps) | - | - |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
stages:
  build:
    name: Build Stage
    fail_fast: true
    jobs:
      build:
        name: Build job
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Build step
            run: |
              echo "build_done"
  test:
    name: Test Stage
    fail_fast: false
    jobs:
      test:
        name: Test job
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Test step
            run: |
              echo "test_done"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] stages map 格式通过校验 | ❌ NOT_COVERED | no steps found |
| [正向] 单 stage 可缺省 stages 字段 | ❌ NOT_COVERED | no steps found |
| [正向] fail_fast true 时某 job 失败中断后续 stage | ❌ NOT_COVERED | no steps found |

### 问题

- [正向] stages map 格式通过校验: NOT_COVERED - no steps found
- [正向] 单 stage 可缺省 stages 字段: NOT_COVERED - no steps found
- [正向] fail_fast true 时某 job 失败中断后续 stage: NOT_COVERED - no steps found

---
