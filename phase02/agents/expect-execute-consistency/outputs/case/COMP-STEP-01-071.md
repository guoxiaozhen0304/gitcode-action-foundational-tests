# COMP-STEP-01-071

- **标题**: step 执行控制 shell working-directory continue-on-error timeout-minutes 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**step 执行控制 shell working-directory continue-on-error timeout-minutes 验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069

通过标准：
1. type=positive, target=run_logs, must_contain="bash_ok"
2. type=positive, target=run_logs, must_contain="sh_ok"
3. type=positive, target=run_logs, must_contain="wd_ok"
4. type=positive, target=run_logs, must_contain="continue_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Bash shell | `echo "bash_ok"` |  | ❌ VACUOUS |
| 2 | Sh shell | `echo "sh_ok"` |  | ❌ VACUOUS |
| 3 | Working directory | `echo "wd_ok"` |  | ❌ VACUOUS |
| 4 | Continue on error | `echo "continue_ok"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

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

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=bash_ok | ❌ VACUOUS | bash_ok: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=sh_ok | ❌ VACUOUS | sh_ok: VACUOUS (步骤仅 echo，未执行功能) |
| 3 | run_logs | positive | must_contain=wd_ok | ❌ VACUOUS | wd_ok: VACUOUS (步骤仅 echo，未执行功能) |
| 4 | run_logs | positive | must_contain=continue_ok | ✅ GENUINE | continue_ok: GENUINE |

### 问题

**断言 1 — VACUOUS**❌: bash_ok: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — VACUOUS**❌: sh_ok: VACUOUS (步骤仅 echo，未执行功能)

**断言 3 — VACUOUS**❌: wd_ok: VACUOUS (步骤仅 echo，未执行功能)

---