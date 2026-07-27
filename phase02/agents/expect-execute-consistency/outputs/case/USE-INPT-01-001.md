# USE-INPT-01-001

- **标题**: 使用 string 类型 input 时正常通过校验
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**使用 string 类型 input 时正常通过校验**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-008

通过标准：
1. type=positive, target=run_status, equals=COMPLETED

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo input | `echo "env=${{ inputs.env }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      env:
        description: target environment
        type: string
        required: true
        default: staging
jobs:
  test-input:
    name: test string input
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo input
        run: |
          echo "env=${{ inputs.env }}"
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
| 1 | run_status | positive | equals=COMPLETED | ❌ IMPOSSIBLE | 期望 !=success 但无步骤可能失败 |

### 问题

**断言 1 — IMPOSSIBLE**❌: 期望 !=success 但无步骤可能失败

---