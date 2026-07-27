# REL-QUEUE-01-003

- **标题**: concurrency QUEUE 策略——超上限运行应排队等待
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**concurrency QUEUE 策略——超上限运行应排队等待**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-003

通过标准：
1. type=positive, target=run_status, equals=completed(success)
2. type=nonfunctional, target=queued_count, equals=2

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 30` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
concurrency:
  max: 2
  exceed-action: QUEUE
jobs:
  test:
    name: concurrency test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 30
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
| 1 | run_status | positive | equals=completed(success) | ✅ GENUINE | 状态断言 completed(success) 可被步骤行为验证 |
| 2 | queued_count | nonfunctional | equals=2 | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---