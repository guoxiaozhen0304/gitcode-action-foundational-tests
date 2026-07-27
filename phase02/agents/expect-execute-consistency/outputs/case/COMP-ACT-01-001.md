# COMP-ACT-01-001

- **标题**: action inputs.required 未传参时平台不自动校验
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**action inputs.required 未传参时平台不自动校验**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-026

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, must_contain="REQ_INPUT_EMPTY"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Call without required inp | `./.gitcode/actions/req-check` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  callaction:
    name: Call local action missing required
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Call without required input
        uses: ./.gitcode/actions/req-check
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `local-action-required` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | must_contain=REQ_INPUT_EMPTY | ✅ GENUINE | REQ_INPUT_EMPTY: GENUINE (uses action 内部输出) |

---