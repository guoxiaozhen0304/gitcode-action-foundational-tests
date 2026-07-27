# COMPAT-ISOLATE-01-002

- **标题**: Runner 环境隔离——跨 job 环境变量隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**Runner 环境隔离——跨 job 环境变量隔离**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-028

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=negative, target=run_logs, eval=llm_assisted
3. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) set env in job A | `echo "ISOLATION_TEST_KEY=VALUE_FROM_JOB_A" >> "$ATOMGIT_ENV" echo "ENV_SET_IN_JO` |  | ❌ VACUOUS |
| 2 | (TC) verify env not leake | `if [ "${ISOLATION_TEST_KEY:-}" = "VALUE_FROM_JOB_A" ]; then   echo "ENV_ISOLATIO` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-set-env:
    name: Set environment variable
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) set env in job A
        run: |
          echo "ISOLATION_TEST_KEY=VALUE_FROM_JOB_A" >> "$ATOMGIT_ENV"
          echo "ENV_SET_IN_JOB_A"
  job-verify-env:
    name: Verify env isolation
    runs-on: [ubuntu-latest, x64, small]
    needs: job-set-env
    steps:
      - name: (TC) verify env not leaked
        run: |
          if [ "${ISOLATION_TEST_KEY:-}" = "VALUE_FROM_JOB_A" ]; then
            echo "ENV_ISOLATION_BROKEN"
            exit 1
          else
            echo "ENV_ISOLATED_OK"
          fi
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
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---