# USE-DOC-01-004

- **标题**: workflow-commands 多行输出示例漏写重定向照抄得空输出
- **维度**: 易用性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**workflow-commands 多行输出示例漏写重定向照抄得空输出**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-033

通过标准：
1. type=positive, target=run_logs, eval=deterministic
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | doc example produce outpu | `echo "multiline<<EOF" echo "line1" echo "line2" echo "EOF"` |  | ❌ VACUOUS |
| 2 | read output | `echo "got=[${{ steps.producer.outputs.multiline }}]"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: multiline output doc example
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: doc example produce output
        id: producer
        run: |
          echo "multiline<<EOF"
          echo "line1"
          echo "line2"
          echo "EOF"
      - name: read output
        run: |
          echo "got=[${{ steps.producer.outputs.multiline }}]"
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
| 1 | run_logs | positive | eval=deterministic | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---