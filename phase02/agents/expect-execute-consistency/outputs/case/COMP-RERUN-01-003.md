# COMP-RERUN-01-003

- **标题**: 超过 6 小时的运行不可 rerun
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**超过 6 小时的运行不可 rerun**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-009

通过标准：
1. type=negative, target=rerun_result, equals=rerun_of_6h_plus_run

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo | `echo "run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify rerun age limit
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo
        run: |
          echo "run"
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
| 1 | rerun_result | negative | equals=rerun_of_6h_plus_run | ✅ GENUINE | 断言有条件可被步骤验证 |

---