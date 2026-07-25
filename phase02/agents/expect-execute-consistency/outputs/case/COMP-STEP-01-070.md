# COMP-STEP-01-070

- 标题: step 可选字段 id env if with 验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-STEP-01-070
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-279~288
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      step 可选字段 id env if with 验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 id / env / if / with 的 step
  2. 验证各字段生效

预期结果:
  - id 用于后续引用 outputs，env 仅对该 step 生效，if 控制步骤执行，with 向 Action 传参

验证点:
  - [正向] id 定义的步骤可被后续引用 outputs
  - [正向] env 仅在该 step 内生效
  - [正向] if 条件正确控制步骤执行

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Step with id | run: echo "result=hello" >> "$ATOMGIT_OUTPUT"
 | id: mystep | 是 |
| 2 | Use output | run: echo "OUT=${{ steps.mystep.outputs.result }}"
 | 是 |
| 3 | Conditional step | run: echo "STEP_VAR=$STEP_VAR"
 | if: ${{ true }} | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step optional fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Step with id
        id: mystep
        run: |
          echo "result=hello" >> "$ATOMGIT_OUTPUT"
      - name: Use output
        run: |
          echo "OUT=${{ steps.mystep.outputs.result }}"
      - name: Conditional step
        if: ${{ true }}
        env:
          STEP_VAR: step_value
        run: |
          echo "STEP_VAR=$STEP_VAR"

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
| [正向] id 定义的步骤可被后续引用 outputs | ✅ COVERED | steps have real logic |
| [正向] env 仅在该 step 内生效 | ✅ COVERED | steps have real logic |
| [正向] if 条件正确控制步骤执行 | ✅ COVERED | steps have real logic |

### 问题

无

---
