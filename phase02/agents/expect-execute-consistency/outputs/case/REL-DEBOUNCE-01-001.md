# REL-DEBOUNCE-01-001

- **标题**: 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账**

- 触发事件: `push`
- 规格引用: INTENT-REL-073

通过标准：
1. type=positive, target=push_sha_run_mapping, equals=1:1_or_documented_debounce
2. type=positive, target=same_sha_duplicate_runs_count, equals=0
3. type=negative, target=unexplained_run_loss_detected, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | record sha step | `echo "trigger_sha=${{ atomgit.sha }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  test:
    name: debounce probe job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: record sha step
        run: |
          echo "trigger_sha=${{ atomgit.sha }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | push_sha_run_mapping | positive | equals=1:1_or_documented_debounce | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | same_sha_duplicate_runs_count | positive | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | unexplained_run_loss_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

---