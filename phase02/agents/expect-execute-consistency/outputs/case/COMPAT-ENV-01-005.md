# COMPAT-ENV-01-005

- **标题**: RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-044

通过标准：
1. type=positive, target=run_logs, must_contain="PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo RUNNER identificatio | `echo "RUNNER_OS=[$RUNNER_OS]" echo "RUNNER_ARCH=[$RUNNER_ARCH]" echo "RUNNER_NAM` |  | ❌ VACUOUS |
| 2 | Echo RUNNER path and capa | `echo "RUNNER_TEMP=[$RUNNER_TEMP]" echo "RUNNER_TOOL_CACHE=[$RUNNER_TOOL_CACHE]" ` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe RUNNER series env vars
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo RUNNER identification vars
        run: |
          echo "RUNNER_OS=[$RUNNER_OS]"
          echo "RUNNER_ARCH=[$RUNNER_ARCH]"
          echo "RUNNER_NAME=[$RUNNER_NAME]"
      - name: Echo RUNNER path and capability vars
        run: |
          echo "RUNNER_TEMP=[$RUNNER_TEMP]"
          echo "RUNNER_TOOL_CACHE=[$RUNNER_TOOL_CACHE]"
          echo "RUNNER_ENVIRONMENT=[$RUNNER_ENVIRONMENT]"
          echo "PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=PROBE_DONE | ❌ VACUOUS | PROBE_DONE: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — VACUOUS**❌: PROBE_DONE: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---