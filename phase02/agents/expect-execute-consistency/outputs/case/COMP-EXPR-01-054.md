# COMP-EXPR-01-054

- **标题**: 字符串函数 contains startsWith endsWith 边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**字符串函数 contains startsWith endsWith 边界行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-054

通过标准：
1. type=positive, target=run_logs, must_contain="contains_passed"
2. type=positive, target=run_logs, must_contain="startswith_passed"
3. type=positive, target=run_logs, must_contain="endswith_passed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Contains match | `echo "contains_passed"` | ${{ contains(atomgit.ref_ | ✅ GENUINE |
| 2 | StartsWith match | `echo "startswith_passed"` | ${{ startsWith(atomgit.re | ✅ GENUINE |
| 3 | EndsWith match | `echo "endswith_passed"` | ${{ endsWith(atomgit.ref_ | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify string functions boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Contains match
        if: ${{ contains(atomgit.ref_name, 'main') }}
        run: |
          echo "contains_passed"
      - name: StartsWith match
        if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}
        run: |
          echo "startswith_passed"
      - name: EndsWith match
        if: ${{ endsWith(atomgit.ref_name, 'ain') }}
        run: |
          echo "endswith_passed"
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
| 1 | run_logs | positive | must_contain=contains_passed | ✅ GENUINE | contains_passed: GENUINE |
| 2 | run_logs | positive | must_contain=startswith_passed | ✅ GENUINE | startswith_passed: GENUINE |
| 3 | run_logs | positive | must_contain=endswith_passed | ✅ GENUINE | endswith_passed: GENUINE |

---