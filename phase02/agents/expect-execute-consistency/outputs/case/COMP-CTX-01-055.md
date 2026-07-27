# COMP-CTX-01-055

- **标题**: workflow_dispatch 触发下 inputs 正常求值（回归保护）
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**workflow_dispatch 触发下 inputs 正常求值（回归保护）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-020

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, must_contain="DISPATCH_INPUT=default-pr"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo dispatch input | `echo "DISPATCH_INPUT=${{ inputs.pr_id }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      pr_id:
        description: PR id
        default: default-pr
jobs:
  probe:
    name: Probe dispatch inputs
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo dispatch input
        run: |
          echo "DISPATCH_INPUT=${{ inputs.pr_id }}"
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
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | must_contain=DISPATCH_INPUT=default-pr | ❌ MISSING_SOURCE | DISPATCH_INPUT=default-pr: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 2 — MISSING_SOURCE**❌: DISPATCH_INPUT=default-pr: MISSING_SOURCE (无步骤产出此字符串)

---