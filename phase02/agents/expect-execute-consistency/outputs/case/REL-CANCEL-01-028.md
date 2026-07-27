# REL-CANCEL-01-028

- **标题**: 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**手动取消 workflow——运行中取消时 always() cleanup step 仍应执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-028

通过标准：
1. type=positive, target=cleanup_step_status, equals=success
2. type=positive, target=run_status, equals=canceled

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep main step | `sleep 60` |  | ✅ GENUINE |
| 2 | cleanup always step | `echo cleanup executed` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: cancel semantics test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep main step
        run: |
          sleep 60
      - name: cleanup always step
        if: ${{ always() }}
        run: |
          echo cleanup executed
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
| 1 | cleanup_step_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_status | positive | equals=canceled | ✅ GENUINE | 状态断言 canceled 可被步骤行为验证 |

---