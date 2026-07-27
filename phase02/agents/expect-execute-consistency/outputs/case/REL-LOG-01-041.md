# REL-LOG-01-041

- **标题**: 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-077

通过标准：
1. type=positive, target=log_downloadable, equals=true
2. type=positive, target=tail_integrity, equals=complete_or_explicitly_marked_truncated
3. type=negative, target=silent_tail_loss_detected, equals=true
4. type=nonfunctional, target=measured_log_limit, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | emit numbered log step | `seq -f "LOG_LINE_%08.0f xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 8000000` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: big log probe job
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 120
    steps:
      - name: emit numbered log step
        run: |
          seq -f "LOG_LINE_%08.0f xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 8000000
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
| 1 | log_downloadable | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | tail_integrity | positive | equals=complete_or_explicitly_marked_truncated | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | silent_tail_loss_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | measured_log_limit | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---