# COMP-STATUS-01-001

- **标题**: 运行状态机 queued 到 completed 转换正确
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**运行状态机 queued 到 completed 转换正确**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-017

通过标准：
1. type=positive, target=run_status_sequence, equals=queued_in_progress_completed
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo | `echo "running"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify status transitions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo
        run: |
          echo "running"
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
| 1 | run_status_sequence | positive | equals=queued_in_progress_completed | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |

### 问题

**断言 2 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

---