# COMPAT-EXPR-01-003

- **标题**: failure() 与 failed 关键字的处理行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**failure() 与 failed 关键字的处理行为差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-005

通过标准：
1. type=positive, target=run_logs, contains="Cleanup ran after failure"
2. type=positive, target=run_status, equals=failure

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | force failure | `exit 1` |  | ✅ GENUINE |
| 3 | cleanup after failure | `echo "Cleanup ran after failure"` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-failure:
    name: Test failure handling
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: force failure
        run: |
          exit 1
      - name: cleanup after failure
        if: ${{ always() }}
        run: |
          echo "Cleanup ran after failure"
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
| 1 | run_logs | positive | contains=Cleanup ran after failure | ✅ GENUINE | Cleanup ran after failure: GENUINE |
| 2 | run_status | positive | equals=failure | ✅ GENUINE | 存在故意失败步骤或 continue-on-error |

---