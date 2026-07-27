# COMPAT-NEEDS-01-002

- **标题**: needs 上游 job 被跳过时的 result 取值语义
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**needs 上游 job 被跳过时的 result 取值语义**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-041

通过标准：
1. type=positive, target=run_logs, must_contain="PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Never executed | `echo "SHOULD_NOT_PRINT"` |  | ❌ VACUOUS |
| 2 | Read result of skipped up | `echo "SKIPPED_RESULT=${{ needs.skipme.result }}" echo "PROBE_DONE"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  skipme:
    name: Upstream job always skipped
    if: ${{ false }}
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Never executed
        run: |
          echo "SHOULD_NOT_PRINT"
  downstream:
    name: Downstream reads skipped result
    needs: skipme
    if: ${{ always() }}
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Read result of skipped upstream
        run: |
          echo "SKIPPED_RESULT=${{ needs.skipme.result }}"
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
| 1 | run_logs | positive | must_contain=PROBE_DONE | ✅ GENUINE | PROBE_DONE: GENUINE |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---