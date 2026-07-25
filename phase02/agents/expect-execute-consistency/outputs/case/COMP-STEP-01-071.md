# COMP-STEP-01-071

- 标题: step 执行控制 shell working-directory continue-on-error timeout-minutes 验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-STEP-01-071
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-279~288
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      step 执行控制 shell working-directory continue-on-error timeout-minutes 验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 shell / working-directory / continue-on-error / timeout-minutes 的 step
  2. 验证各字段生效

预期结果:
  - shell 指定执行器，working-directory 指定执行目录，continue-on-error true 时步骤失败不终止 job，timeout-minutes 限制步骤时长

验证点:
  - [正向] shell bash 和 sh 均可执行
  - [正向] working-directory 改变执行目录
  - [正向] continue-on-error true 被接受

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Bash shell | run: echo "bash_ok"
 | 否 |
| 2 | Sh shell | run: echo "sh_ok"
 | 否 |
| 3 | Working directory | run: echo "wd_ok"
 | 否 |
| 4 | Continue on error | run: echo "continue_ok"
 | continue-on-error: true | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step execution control
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Bash shell
        shell: bash
        run: |
          echo "bash_ok"
      - name: Sh shell
        shell: sh
        run: |
          echo "sh_ok"
      - name: Working directory
        working-directory: .
        run: |
          echo "wd_ok"
      - name: Continue on error
        continue-on-error: true
        run: |
          echo "continue_ok"

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
| [正向] shell bash 和 sh 均可执行 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] working-directory 改变执行目录 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] continue-on-error true 被接受 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] shell bash 和 sh 均可执行: PARTIAL - all steps are trivial echo
- [正向] working-directory 改变执行目录: PARTIAL - all steps are trivial echo
- [正向] continue-on-error true 被接受: PARTIAL - all steps are trivial echo

---
