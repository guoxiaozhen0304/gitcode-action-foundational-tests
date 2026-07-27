# COMPAT-PR-01-009

- **标题**: pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-039

通过标准：
1. type=positive, target=run_logs, must_contain="PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Record context sha and re | `echo "CTX_SHA=${{ atomgit.sha }}" echo "CTX_REF=${{ atomgit.ref }}" echo "ENV_SH` |  | ✅ GENUINE |
| 2 | (TC) checkout source | `checkout` |  | ✅ GENUINE |
| 3 | Record checked out commit | `echo "CHECKOUT_HEAD=$(git rev-parse HEAD)" echo "PROBE_DONE"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  probe:
    name: Probe pull_request sha ref semantics
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Record context sha and ref
        run: |
          echo "CTX_SHA=${{ atomgit.sha }}"
          echo "CTX_REF=${{ atomgit.ref }}"
          echo "ENV_SHA=$ATOMGIT_SHA"
      - name: (TC) checkout source
        uses: checkout
      - name: Record checked out commit
        run: |
          echo "CHECKOUT_HEAD=$(git rev-parse HEAD)"
          echo "PROBE_DONE"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-pull-request` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=PROBE_DONE | ✅ GENUINE | PROBE_DONE: GENUINE |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---