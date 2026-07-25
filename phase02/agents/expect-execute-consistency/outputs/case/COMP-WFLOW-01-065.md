# COMP-WFLOW-01-065

- 标题: workflow post 后处理阶段字段验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-WFLOW-01-065
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-366~401
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow post 后处理阶段字段验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 post 阶段的 workflow
  2. 验证 run_always 默认 true 和 false 时的行为

预期结果:
  - post 阶段在 workflow 结束后执行，run_always 为 true 时无论成败都执行，为 false 时仅成功时执行

验证点:
  - [正向] post 步骤在成功时执行
  - [正向] run_always true 时失败 workflow 仍执行 post

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Main step | run: echo "main_done"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Main job
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Main step
        run: |
          echo "main_done"
post:
  run_always: true
  steps:
    - name: Post notification
      run: |
        echo "post_done"

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
| [正向] post 步骤在成功时执行 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] run_always true 时失败 workflow 仍执行 post | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] post 步骤在成功时执行: PARTIAL - all steps are trivial echo
- [正向] run_always true 时失败 workflow 仍执行 post: PARTIAL - all steps are trivial echo

---
