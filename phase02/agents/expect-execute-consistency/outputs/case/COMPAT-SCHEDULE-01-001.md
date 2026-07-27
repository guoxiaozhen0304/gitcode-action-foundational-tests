# COMPAT-SCHEDULE-01-001

- **标题**: schedule cron 按 UTC 时间触发
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**schedule cron 按 UTC 时间触发**

- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-013

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_event, equals=schedule
3. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo schedule time | `echo "SCHEDULE_TRIGGER_OK" echo "Current UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    cron: "0 12 * * *"
jobs:
  verify:
    name: Verify schedule UTC trigger
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo schedule time
        run: |
          echo "SCHEDULE_TRIGGER_OK"
          echo "Current UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
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
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | run_event | positive | equals=schedule | ✅ GENUINE | 事件断言与 trigger.event=schedule 一致 |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---