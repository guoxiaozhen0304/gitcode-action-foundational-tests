# USE-SECNAME-01-001

- **标题**: Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-028

通过标准：
1. type=negative, target=run_status, equals=COMPLETED
2. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | use reserved prefix secre | `echo "token=${{ secrets.ATOMGIT_TOKEN }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  bad:
    name: secret name rule violation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: use reserved prefix secret
        run: |
          echo "token=${{ secrets.ATOMGIT_TOKEN }}"
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
| 1 | run_status | negative | equals=COMPLETED | ❌ IMPOSSIBLE | 期望 !=success 但无步骤可能失败 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — IMPOSSIBLE**❌: 期望 !=success 但无步骤可能失败

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---