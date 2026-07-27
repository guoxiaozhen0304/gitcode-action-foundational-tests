# USE-LBL-01-004

- **标题**: quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证
- **维度**: 易用性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-031

通过标准：
1. type=positive, target=run_status, equals=success
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | hello step | `echo "hello from single-label runs-on"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: quick-start single label runs-on
    runs-on: ubuntu-latest
    steps:
      - name: hello step
        run: |
          echo "hello from single-label runs-on"
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
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

---