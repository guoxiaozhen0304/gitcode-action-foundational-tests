# COMP-PUSH-01-002

- **标题**: 不匹配 branches 的 push 不触发 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**不匹配 branches 的 push 不触发 workflow**

- 触发事件: `push`
- 规格引用: INTENT-COMP-003

通过标准：
1. type=negative, target=run_created, equals=no_run_for_non_matching_branch

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo triggered | `echo "should not run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches:
      - main
jobs:
  verify:
    name: Verify branch skip
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo triggered
        run: |
          echo "should not run"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | equals=no_run_for_non_matching_branch | ✅ GENUINE | 断言有条件可被步骤验证 |

---