# COMPAT-MASK-01-002

- **标题**: 通过 env 注入 secret 后输出应在日志中被脱敏
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**通过 env 注入 secret 后输出应在日志中被脱敏**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-033

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="TEST_SECRET", eval=deterministic
2. type=positive, target=run_logs, eval=llm_assisted
3. type=positive, target=run_status, equals=success, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | echo secret via env | `echo "Env value: $MY_VAR"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  mask-env-test:
    name: Test secret masking via env
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: echo secret via env
        env:
          MY_VAR: ${{ secrets.TEST_SECRET }}
        run: |
          echo "Env value: $MY_VAR"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['TEST_SECRET']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=TEST_SECRET | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 TEST_SECRET |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_status | positive | equals=success | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 TEST_SECRET

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---