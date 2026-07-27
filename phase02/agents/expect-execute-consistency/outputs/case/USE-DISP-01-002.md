# USE-DISP-01-002

- **标题**: workflow_dispatch 未提供参数但存在 default 时应使用默认值运行
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**workflow_dispatch 未提供参数但存在 default 时应使用默认值运行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-030

通过标准：
1. type=positive, target=run_logs, contains="env=staging"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo env | `echo "env=${{ inputs.environment }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: target environment
        type: string
        required: false
        default: staging
jobs:
  test-default:
    name: default input value
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo env
        run: |
          echo "env=${{ inputs.environment }}"
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
| 1 | run_logs | positive | contains=env=staging | ❌ MISSING_SOURCE | env=staging: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: env=staging: MISSING_SOURCE (无步骤产出此字符串)

---