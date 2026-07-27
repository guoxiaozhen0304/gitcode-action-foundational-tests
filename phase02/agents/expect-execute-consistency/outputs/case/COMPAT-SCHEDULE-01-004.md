# COMPAT-SCHEDULE-01-004

- **标题**: schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认**

- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-051

通过标准：
1. type=positive, target=run_logs, must_contain="SCHEDULE_PROBE_DONE"
2. type=negative, target=run_list, eval=llm_assisted
3. type=nonfunctional, target=run_list, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Record actual trigger tim | `date -u +"ACTUAL_TRIGGER_UTC=%Y-%m-%dT%H:%M:%SZ" echo "SCHEDULE_PROBE_DONE"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "*/5 * * * *"
jobs:
  probe:
    name: Probe schedule lifecycle semantics
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Record actual trigger time
        run: |
          date -u +"ACTUAL_TRIGGER_UTC=%Y-%m-%dT%H:%M:%SZ"
          echo "SCHEDULE_PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=SCHEDULE_PROBE_DONE | ✅ GENUINE | SCHEDULE_PROBE_DONE: GENUINE |
| 2 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_list | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---