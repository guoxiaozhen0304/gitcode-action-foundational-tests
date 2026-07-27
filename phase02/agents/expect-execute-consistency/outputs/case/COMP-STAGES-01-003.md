# COMP-STAGES-01-003

- **标题**: post.run_always true 时 workflow 失败仍执行 post
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**post.run_always true 时 workflow 失败仍执行 post**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007

通过标准：
1. type=positive, target=run_status, equals=failure
2. type=positive, target=post_logs, contains="post executed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Force failure | `exit 1` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  main:
    name: Main job fail
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Force failure
        run: |
          exit 1
post:
  run_always: true
  steps:
    - name: Post cleanup
      run: |
        echo "post executed"
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
| 1 | run_status | positive | equals=failure | ✅ GENUINE | 存在故意失败步骤或 continue-on-error |
| 2 | post_logs | positive | contains=post executed | ✅ GENUINE | 断言有条件可被步骤验证 |

---