# COMP-VARREF-01-084

- **标题**: ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-032

通过标准：
1. type=positive, target=run_logs, must_contain="GC_LIT="
2. type=positive, target=run_logs, must_contain="PL_LIT="
3. type=nonfunctional, target=interpolation_eval, eval=llm_assisted
4. type=negative, target=silent_literal, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Probe interpolation style | `echo 'GC_LIT=${gitcode_SOURCE_BRANCH}' echo 'PL_LIT=${PIPELINE_RUN_ID}' echo "GC` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe legacy interpolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Probe interpolation styles
        run: |
          echo 'GC_LIT=${gitcode_SOURCE_BRANCH}'
          echo 'PL_LIT=${PIPELINE_RUN_ID}'
          echo "GC_SHELL=${gitcode_SOURCE_BRANCH}"
          echo "PL_SHELL=${PIPELINE_RUN_ID}"
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
| 1 | run_logs | positive | must_contain=GC_LIT= | ❌ VACUOUS | GC_LIT=: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=PL_LIT= | ❌ VACUOUS | PL_LIT=: VACUOUS (步骤仅 echo，未执行功能) |
| 3 | interpolation_eval | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | silent_literal | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — VACUOUS**❌: GC_LIT=: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — VACUOUS**❌: PL_LIT=: VACUOUS (步骤仅 echo，未执行功能)

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---