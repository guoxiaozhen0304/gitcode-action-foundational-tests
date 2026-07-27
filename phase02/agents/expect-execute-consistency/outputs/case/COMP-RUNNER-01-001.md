# COMP-RUNNER-01-001

- **标题**: 三段式标签正确调度到对应规格 Runner
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**三段式标签正确调度到对应规格 Runner**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-010

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=runner_label, equals=ubuntu-latest,x64,small

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo runner info | `echo "os=$RUNNER_OS" echo "arch=$RUNNER_ARCH"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify 3 segment label
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo runner info
        run: |
          echo "os=$RUNNER_OS"
          echo "arch=$RUNNER_ARCH"
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
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | runner_label | positive | equals=ubuntu-latest,x64,small | ✅ GENUINE | 断言有条件可被步骤验证 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

---