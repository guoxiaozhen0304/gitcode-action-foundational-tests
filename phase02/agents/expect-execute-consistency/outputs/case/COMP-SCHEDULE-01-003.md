# COMP-SCHEDULE-01-003

- **标题**: cron 间隔短于 5 分钟时被拒绝或降级
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cron 间隔短于 5 分钟时被拒绝或降级**

- 触发事件: `schedule`
- 规格引用: INTENT-COMP-005

通过标准：
1. type=negative, target=run_status, equals=success_with_1min_interval
2. type=nonfunctional, target=error_message, eval=llm_assisted

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
    - cron: "*/1 * * * *"
jobs:
  verify:
    name: Verify short interval rejection
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
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals=success_with_1min_interval | ✅ GENUINE | 状态断言 success_with_1min_interval 可被步骤行为验证 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---