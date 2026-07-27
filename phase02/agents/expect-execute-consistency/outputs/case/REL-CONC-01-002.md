# REL-CONC-01-002

- **标题**: concurrency.max=6 配置应被系统拒绝
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**concurrency.max=6 配置应被系统拒绝**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-002

通过标准：
1. type=positive, target=yaml_validation, equals=rejected
2. type=negative, target=run_status, equals=should_not_start

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 10` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
concurrency:
  max: 6
  exceed-action: QUEUE
jobs:
  test:
    name: concurrency test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 10
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
| 2 | run_status | negative | equals=should_not_start | ✅ GENUINE | 状态断言 should_not_start 可被步骤行为验证 |

---