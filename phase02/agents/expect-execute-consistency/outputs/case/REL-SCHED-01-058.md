# REL-SCHED-01-058

- **标题**: schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性**

- 触发事件: `schedule`
- 规格引用: INTENT-REL-085

通过标准：
1. type=positive, target=runs_on_default_branch_head, equals=true
2. type=positive, target=duplicate_trigger_count, equals=0
3. type=negative, target=non_default_branch_triggered, equals=true
4. type=nonfunctional, target=trigger_loss_rate_pct
5. type=nonfunctional, target=trigger_delay_p95_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | tick step | `echo "schedule_tick $(date -u +%FT%TZ)"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "*/5 * * * *"
jobs:
  tick:
    name: schedule tick job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: tick step
        run: |
          echo "schedule_tick $(date -u +%FT%TZ)"
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
| 1 | runs_on_default_branch_head | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | duplicate_trigger_count | positive | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | non_default_branch_triggered | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | trigger_loss_rate_pct | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 5 | trigger_delay_p95_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 5 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---