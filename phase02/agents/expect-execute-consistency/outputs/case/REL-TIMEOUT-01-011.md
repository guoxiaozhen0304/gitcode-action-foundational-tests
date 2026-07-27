# REL-TIMEOUT-01-011

- **标题**: 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-075

通过标准：
1. type=positive, target=config_outcome, equals=accepted_or_explicitly_rejected
2. type=negative, target=silent_truncation_to_360_detected, equals=true
3. type=nonfunctional, target=rejection_error_contains_limit, equals=true_if_rejected

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | timeout probe step | `echo "timeout_720_probe_marker"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: timeout 720 probe job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 720
    steps:
      - name: timeout probe step
        run: |
          echo "timeout_720_probe_marker"
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
| 1 | config_outcome | positive | equals=accepted_or_explicitly_rejected | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | silent_truncation_to_360_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | rejection_error_contains_limit | nonfunctional | equals=true_if_rejected | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---