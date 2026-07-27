# COMP-EXPR-01-057

- **标题**: format substring replace 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**format substring replace 函数边界行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-057

通过标准：
1. type=positive, target=run_logs, must_contain="FMT=Hello World"
2. type=positive, target=run_logs, must_contain="SUB="
3. type=positive, target=run_logs, must_contain="REP="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Format string | `echo "FMT=${{ format('Hello {0}', 'World') }}"` |  | ✅ GENUINE |
| 2 | Substring sha | `echo "SUB=${{ substring(atomgit.sha, 0, 7) }}"` |  | ✅ GENUINE |
| 3 | Replace prefix | `echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify format substring replace
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Format string
        run: |
          echo "FMT=${{ format('Hello {0}', 'World') }}"
      - name: Substring sha
        run: |
          echo "SUB=${{ substring(atomgit.sha, 0, 7) }}"
      - name: Replace prefix
        run: |
          echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}"
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
| 1 | run_logs | positive | must_contain=FMT=Hello World | ❌ MISSING_SOURCE | FMT=Hello World: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=SUB= | ✅ GENUINE | SUB=: GENUINE |
| 3 | run_logs | positive | must_contain=REP= | ✅ GENUINE | REP=: GENUINE |

### 问题

**断言 1 — MISSING_SOURCE**❌: FMT=Hello World: MISSING_SOURCE (无步骤产出此字符串)

---