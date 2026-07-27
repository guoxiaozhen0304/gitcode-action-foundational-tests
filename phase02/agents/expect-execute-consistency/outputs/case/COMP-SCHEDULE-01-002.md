# COMP-SCHEDULE-01-002

- **标题**: 非默认分支的 schedule workflow 不应触发
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**非默认分支的 schedule workflow 不应触发**

- 触发事件: `schedule`
- 规格引用: INTENT-COMP-005

通过标准：
1. type=negative, target=run_created, equals=no_run_on_non_default_branch

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo scheduled | `echo "should not run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule non default branch
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo scheduled
        run: |
          echo "should not run"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `schedule` |
| 触发身份 | `maintainer` |
| Repo 环境 | `multi-branch` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | equals=no_run_on_non_default_branch | ✅ GENUINE | 断言有条件可被步骤验证 |

---