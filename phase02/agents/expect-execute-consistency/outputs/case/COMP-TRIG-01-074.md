# COMP-TRIG-01-074

- **标题**: workflow_dispatch 事件关键字段与 inputs 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**workflow_dispatch 事件关键字段与 inputs 验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-074

通过标准：
1. type=positive, target=run_logs, must_contain="ENV="
2. type=positive, target=run_logs, must_contain="VER="
3. type=positive, target=run_logs, must_contain="dispatch_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print inputs | `echo "ENV=${{ inputs.environment }}" echo "VER=${{ inputs.version }}" echo "disp` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: Target env
        type: string
        required: true
        default: staging
      version:
        description: Version
        type: string
        required: false
        default: 1.0.0
jobs:
  verify:
    name: Verify workflow_dispatch fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print inputs
        run: |
          echo "ENV=${{ inputs.environment }}"
          echo "VER=${{ inputs.version }}"
          echo "dispatch_ok"
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
| 1 | run_logs | positive | must_contain=ENV= | ✅ GENUINE | ENV=: GENUINE |
| 2 | run_logs | positive | must_contain=VER= | ✅ GENUINE | VER=: GENUINE |
| 3 | run_logs | positive | must_contain=dispatch_ok | ✅ GENUINE | dispatch_ok: GENUINE |

---