# USE-STAT-01-001

- **标题**: 使用 always() 带括号时若被接受则正常执行
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**使用 always() 带括号时若被接受则正常执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-004

通过标准：
1. type=positive, target=run_logs, contains="cleanup executed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | force fail | `exit 1` |  | ✅ GENUINE |
| 2 | cleanup with always | `echo "cleanup executed"` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-always:
    name: test always syntax
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: force fail
        run: |
          exit 1
      - name: cleanup with always
        if: ${{ always() }}
        run: |
          echo "cleanup executed"
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
| 1 | run_logs | positive | contains=cleanup executed | ✅ GENUINE | cleanup executed: GENUINE |

---