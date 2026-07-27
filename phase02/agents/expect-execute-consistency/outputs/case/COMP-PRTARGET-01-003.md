# COMP-PRTARGET-01-003

- **标题**: fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-023

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="TEST_SECRET"
2. type=negative, target=secret_injection, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Checkout pr head | `checkout` |  | ✅ GENUINE |
| 2 | Probe secret presence | `if [ -z "$TEST_SECRET" ]; then echo "SECRET_NOT_INJECTED"; else echo "SECRET_INJ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches: [main]
jobs:
  inspect:
    name: Inspect fork pr context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout pr head
        uses: checkout
        with:
          ref: ${{ atomgit.pull_request.head.sha }}
      - name: Probe secret presence
        env:
          TEST_SECRET: "${{ secrets.TEST_SECRET }}"
        run: |
          if [ -z "$TEST_SECRET" ]; then echo "SECRET_NOT_INJECTED"; else echo "SECRET_INJECTED"; fi
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_target` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `fork-pr-target` |
| Secrets | `['TEST_SECRET']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=TEST_SECRET | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 TEST_SECRET |
| 2 | secret_injection | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 TEST_SECRET

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---