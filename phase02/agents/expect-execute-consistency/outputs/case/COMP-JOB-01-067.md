# COMP-JOB-01-067

- **标题**: job 可选字段 env if timeout-minutes needs 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**job 可选字段 env if timeout-minutes needs 验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-066

通过标准：
1. type=positive, target=run_logs, must_contain="prepare_done"
2. type=positive, target=run_logs, must_contain="JOB_VAR=job_value"
3. type=positive, target=run_logs, must_contain="optional_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Prepare | `echo "prepare_done"` |  | ❌ VACUOUS |
| 2 | Check fields | `echo "JOB_VAR=$JOB_VAR" echo "optional_ok"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  prepare:
    name: Prepare job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Prepare
        run: |
          echo "prepare_done"
  verify:
    name: Verify optional fields
    runs-on: [ubuntu-latest, x64, small]
    needs: prepare
    if: ${{ true }}
    timeout-minutes: 30
    env:
      JOB_VAR: job_value
    steps:
      - name: Check fields
        run: |
          echo "JOB_VAR=$JOB_VAR"
          echo "optional_ok"
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
| 1 | run_logs | positive | must_contain=prepare_done | ❌ VACUOUS | prepare_done: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=JOB_VAR=job_value | ❌ MISSING_SOURCE | JOB_VAR=job_value: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=optional_ok | ❌ VACUOUS | optional_ok: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — VACUOUS**❌: prepare_done: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — MISSING_SOURCE**❌: JOB_VAR=job_value: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — VACUOUS**❌: optional_ok: VACUOUS (步骤仅 echo，未执行功能)

---