# COMPAT-WCMD-01-005

- **标题**: debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-042

通过标准：
1. type=positive, target=run_logs, must_contain="DEBUG_PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Emit debug command | `echo "::debug::demo debug message" echo "DEBUG_PROBE_DONE"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe debug command visibility
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Emit debug command
        run: |
          echo "::debug::demo debug message"
          echo "DEBUG_PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=DEBUG_PROBE_DONE | ❌ VACUOUS | DEBUG_PROBE_DONE: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — VACUOUS**❌: DEBUG_PROBE_DONE: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---