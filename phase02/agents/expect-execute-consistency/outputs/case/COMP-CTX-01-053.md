# COMP-CTX-01-053

- **标题**: 上下文在 Action 插件参数中注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**上下文在 Action 插件参数中注入验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Checkout with explicit to | `checkout` |  | ✅ GENUINE |
| 2 | Echo env in action param | `echo "done"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify context in Action with params
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout with explicit token
        uses: checkout
        with:
          ref: ${{ atomgit.ref }}
      - name: Echo env in action param
        run: |
          echo "done"
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

---