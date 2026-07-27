# REL-PREEMPT-01-006

- **标题**: preemption events 越界值——配置 11 个应被拒绝
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**preemption events 越界值——配置 11 个应被拒绝**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-006

通过标准：
1. type=positive, target=yaml_validation, equals=rejected

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo step | `echo test` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
concurrency:
  max: 5
  exceed-action: QUEUE
  preemption:
    events: [push, pull_request, workflow_dispatch, schedule, tag, issue_comment, pull_request_comment, merge_requests, fork_pr, manual, pr]
jobs:
  test:
    name: preempt invalid test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo step
        run: |
          echo test
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
| 1 | yaml_validation | positive | equals=rejected | ✅ GENUINE | 断言有条件可被步骤验证 |

---