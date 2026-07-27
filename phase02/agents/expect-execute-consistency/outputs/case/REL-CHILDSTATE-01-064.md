# REL-CHILDSTATE-01-064

- **标题**: 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成
- **维度**: 可靠性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-064

通过标准：
1. type=positive, target=parent_status, equals=failure
2. type=positive, target=downstream_status, equals=skipped
3. type=negative, target=parent_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | should not run | `echo downstream` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  call_child:
    name: call failing child workflow
    uses: ./.gitcode/workflows/child_fail.yml
  downstream:
    name: downstream job
    runs-on: [ubuntu-latest, x64, small]
    needs: call_child
    steps:
      - name: should not run
        run: |
          echo downstream
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
| 1 | parent_status | positive | equals=failure | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | downstream_status | positive | equals=skipped | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | parent_status | negative | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |

---