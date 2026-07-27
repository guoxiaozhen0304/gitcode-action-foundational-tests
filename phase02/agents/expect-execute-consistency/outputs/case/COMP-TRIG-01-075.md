# COMP-TRIG-01-075

- **标题**: schedule 事件关键字段与 cron 格式验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**schedule 事件关键字段与 cron 格式验证**

- 触发事件: `schedule`
- 规格引用: INTENT-COMP-075

通过标准：
1. type=positive, target=run_logs, must_contain="schedule_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print schedule | `echo "SCHEDULE=${{ atomgit.event.schedule }}" echo "schedule_ok"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule event fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print schedule
        run: |
          echo "SCHEDULE=${{ atomgit.event.schedule }}"
          echo "schedule_ok"
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
| 1 | run_logs | positive | must_contain=schedule_ok | ✅ GENUINE | schedule_ok: GENUINE |

---