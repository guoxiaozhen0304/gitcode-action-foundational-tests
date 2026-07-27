# COMP-STEP-01-070

- **标题**: step 可选字段 id env if with 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**step 可选字段 id env if with 验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069

通过标准：
1. type=positive, target=run_logs, must_contain="OUT=hello"
2. type=positive, target=run_logs, must_contain="STEP_VAR=step_value"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Step with id | `echo "result=hello" >> "$ATOMGIT_OUTPUT"` |  | ❌ VACUOUS |
| 2 | Use output | `echo "OUT=${{ steps.mystep.outputs.result }}"` |  | ✅ GENUINE |
| 3 | Conditional step | `echo "STEP_VAR=$STEP_VAR"` | ${{ true }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step optional fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Step with id
        id: mystep
        run: |
          echo "result=hello" >> "$ATOMGIT_OUTPUT"
      - name: Use output
        run: |
          echo "OUT=${{ steps.mystep.outputs.result }}"
      - name: Conditional step
        if: ${{ true }}
        env:
          STEP_VAR: step_value
        run: |
          echo "STEP_VAR=$STEP_VAR"
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
| 1 | run_logs | positive | must_contain=OUT=hello | ❌ MISSING_SOURCE | OUT=hello: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=STEP_VAR=step_value | ❌ MISSING_SOURCE | STEP_VAR=step_value: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: OUT=hello: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: STEP_VAR=step_value: MISSING_SOURCE (无步骤产出此字符串)

---