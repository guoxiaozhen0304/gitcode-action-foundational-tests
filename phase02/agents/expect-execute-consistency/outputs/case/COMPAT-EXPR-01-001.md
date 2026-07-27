# COMPAT-EXPR-01-001

- **标题**: success 关键字在条件表达式中的可用性
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**success 关键字在条件表达式中的可用性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004

通过标准：
1. type=positive, target=run_logs, contains="implicit success confirmed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | previous step succeeds | `echo "Step completed successfully"` |  | ❌ VACUOUS |
| 3 | observe next step runs | `echo "Next step executed, implicit success confirmed"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-success:
    name: Test success keyword availability
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: previous step succeeds
        run: |
          echo "Step completed successfully"
      - name: observe next step runs
        run: |
          echo "Next step executed, implicit success confirmed"
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
| 1 | run_logs | positive | contains=implicit success confirmed | ❌ VACUOUS | implicit success confirmed: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — VACUOUS**❌: implicit success confirmed: VACUOUS (步骤仅 echo，未执行功能)

---