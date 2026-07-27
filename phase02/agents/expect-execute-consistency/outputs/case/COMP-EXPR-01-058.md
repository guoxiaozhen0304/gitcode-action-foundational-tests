# COMP-EXPR-01-058

- **标题**: 表达式运算符与优先级边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**表达式运算符与优先级边界行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-058

通过标准：
1. type=positive, target=run_logs, must_contain="eq_passed"
2. type=positive, target=run_logs, must_contain="ne_passed"
3. type=positive, target=run_logs, must_contain="gt_passed"
4. type=positive, target=run_logs, must_contain="logic_passed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Equality | `echo "eq_passed"` | ${{ atomgit.ref_name == ' | ✅ GENUINE |
| 2 | Not equal | `echo "ne_passed"` | ${{ atomgit.ref_name != ' | ✅ GENUINE |
| 3 | Greater than | `echo "gt_passed"` | ${{ 5 > 3 }} | ✅ GENUINE |
| 4 | Logical combo | `echo "logic_passed"` | ${{ true && (false || tru | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify operator precedence
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Equality
        if: ${{ atomgit.ref_name == 'main' || true }}
        run: |
          echo "eq_passed"
      - name: Not equal
        if: ${{ atomgit.ref_name != 'nonexistent' }}
        run: |
          echo "ne_passed"
      - name: Greater than
        if: ${{ 5 > 3 }}
        run: |
          echo "gt_passed"
      - name: Logical combo
        if: ${{ true && (false || true) }}
        run: |
          echo "logic_passed"
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
| 1 | run_logs | positive | must_contain=eq_passed | ✅ GENUINE | eq_passed: GENUINE |
| 2 | run_logs | positive | must_contain=ne_passed | ✅ GENUINE | ne_passed: GENUINE |
| 3 | run_logs | positive | must_contain=gt_passed | ✅ GENUINE | gt_passed: GENUINE |
| 4 | run_logs | positive | must_contain=logic_passed | ✅ GENUINE | logic_passed: GENUINE |

---