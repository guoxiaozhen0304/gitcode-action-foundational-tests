# COMP-WFLOW-01-062

- 标题: workflow env 与 defaults 字段验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-WFLOW-01-062
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-366~401
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow env 与 defaults 字段验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 workflow 级定义 env 和 defaults.run
  2. 在 job 和 step 中验证继承与覆盖

预期结果:
  - workflow 级 env 对所有 job/step 可见，defaults.run.shell 和 working-directory 可被 job/step 覆盖

验证点:
  - [正向] workflow env 在 step 中可访问
  - [正向] defaults shell 被正确继承
  - [正向] step 级 shell 覆盖 defaults

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check global env | run: echo "GLOBAL=$GLOBAL_VAR"
 | 否 |
| 2 | Override shell | run: echo "shell_override"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
env:
  GLOBAL_VAR: global_value
defaults:
  run:
    shell: bash
    working-directory: .
jobs:
  verify:
    name: Verify env and defaults
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check global env
        run: |
          echo "GLOBAL=$GLOBAL_VAR"
      - name: Override shell
        shell: sh
        run: |
          echo "shell_override"

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
| [正向] workflow env 在 step 中可访问 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] defaults shell 被正确继承 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] step 级 shell 覆盖 defaults | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] workflow env 在 step 中可访问: PARTIAL - all steps are trivial echo
- [正向] defaults shell 被正确继承: PARTIAL - all steps are trivial echo
- [正向] step 级 shell 覆盖 defaults: PARTIAL - all steps are trivial echo

---
