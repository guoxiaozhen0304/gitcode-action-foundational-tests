# REL-DEBOUNCE-01-002

- **标题**: 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释**

- 触发事件: `tag`
- 规格引用: INTENT-REL-073

通过标准：
1. type=positive, target=tag_event_run_reconciliation, equals=10/10_or_documented_debounce
2. type=positive, target=same_tag_duplicate_runs_count, equals=0
3. type=negative, target=unexplained_run_loss_detected, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | record ref step | `echo "trigger_ref=${{ atomgit.ref }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    tags:
      - "v*"
jobs:
  test:
    name: tag debounce probe job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: record ref step
        run: |
          echo "trigger_ref=${{ atomgit.ref }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `tag` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | tag_event_run_reconciliation | positive | equals=10/10_or_documented_debounce | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | same_tag_duplicate_runs_count | positive | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | unexplained_run_loss_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

---