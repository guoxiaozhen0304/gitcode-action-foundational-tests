# COMPAT-INPUTS-01-002

- **标题**: workflow_dispatch inputs 类型限制 - string 正常通过
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**workflow_dispatch inputs 类型限制 - string 正常通过**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-014

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, must_contain="STRING_INPUT_OK"
3. type=positive, target=run_logs, must_contain="ENV=production"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo input value | `echo "ENV=${{ inputs.environment }}" echo "STRING_INPUT_OK"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署目标环境'
        required: true
        default: 'staging'
        type: string
jobs:
  verify:
    name: Verify string input acceptance
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo input value
        run: |
          echo "ENV=${{ inputs.environment }}"
          echo "STRING_INPUT_OK"
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
| 2 | run_logs | positive | must_contain=STRING_INPUT_OK | ✅ GENUINE | STRING_INPUT_OK: GENUINE |
| 3 | run_logs | positive | must_contain=ENV=production | ❌ MISSING_SOURCE | ENV=production: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 3 — MISSING_SOURCE**❌: ENV=production: MISSING_SOURCE (无步骤产出此字符串)

---