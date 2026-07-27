# USE-MASK-01-001

- **标题**: secret 脱敏文档描述与实际行为一致并给出缓解建议
- **维度**: 易用性
- **优先级**: P0
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**secret 脱敏文档描述与实际行为一致并给出缓解建议**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-016

通过标准：
1. type=positive, target=run_logs, must_not_contain_secret="TEST_SECRET"
2. type=nonfunctional, target=documentation, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo secret via env | `echo "secret length=${#SECRET_VAL}"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-mask:
    name: test secret masking via env
    runs-on: [ubuntu-latest, x64, small]
    env:
      SECRET_VAL: ${{ secrets.TEST_SECRET }}
    steps:
      - name: echo secret via env
        run: |
          echo "secret length=${#SECRET_VAL}"
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
| 1 | run_logs | positive | !secret=TEST_SECRET | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 TEST_SECRET |
| 2 | documentation | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 TEST_SECRET

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---