# COMPAT-EXPR-01-002

- **标题**: success() 函数的处理行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**success() 函数的处理行为差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004

通过标准：
1. type=positive, target=run_logs, contains="Job B ran after Job A success"
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | succeed | `echo "Job A done"` |  | ❌ VACUOUS |
| 3 | checkout source | `checkout` |  | ✅ GENUINE |
| 4 | observe dependency succes | `echo "Job B ran after Job A success"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-a:
    name: Job A that succeeds
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: succeed
        run: |
          echo "Job A done"
  job-b:
    name: Job B depends on A
    runs-on: [ubuntu-latest, x64, small]
    needs: job-a
    steps:
      - name: checkout source
        uses: checkout
      - name: observe dependency success
        run: |
          echo "Job B ran after Job A success"
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
| 1 | run_logs | positive | contains=Job B ran after Job A success | ❌ VACUOUS | Job B ran after Job A success: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

### 问题

**断言 1 — VACUOUS**❌: Job B ran after Job A success: VACUOUS (步骤仅 echo，未执行功能)

---