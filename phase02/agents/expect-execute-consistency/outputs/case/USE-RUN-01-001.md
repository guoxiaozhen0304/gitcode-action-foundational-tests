# USE-RUN-01-001

- **标题**: 使用三段式标签时 job 正常调度
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**使用三段式标签时 job 正常调度**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-006

通过标准：
1. type=positive, target=run_status, equals=COMPLETED

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | check runner | `echo "runner ok"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-runner:
    name: test three-part labels
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: check runner
        run: |
          echo "runner ok"
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
| 1 | run_status | positive | equals=COMPLETED | ❌ IMPOSSIBLE | 期望 !=success 但无步骤可能失败 |

### 问题

**断言 1 — IMPOSSIBLE**❌: 期望 !=success 但无步骤可能失败

---