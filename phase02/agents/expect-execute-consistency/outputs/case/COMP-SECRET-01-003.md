# COMP-SECRET-01-003

- **标题**: base64 编码后的 secret 是否仍被脱敏
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**base64 编码后的 secret 是否仍被脱敏**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-012

通过标准：
1. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo base64 secret | `echo "base64 secret is $(echo -n '${{ secrets.TEST_SECRET }}' | base64)"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify base64 masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo base64 secret
        run: |
          echo "base64 secret is $(echo -n '${{ secrets.TEST_SECRET }}' | base64)"
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
| 1 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---