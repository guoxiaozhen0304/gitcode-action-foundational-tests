# USE-ENV-01-002

- **标题**: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**引用 GITHUB_SHA 时日志应给出环境变量映射提示**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-003

通过标准：
1. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo GITHUB_SHA | `set -u echo "sha=$GITHUB_SHA"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  bad-env:
    name: test GITHUB env var hint
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo GITHUB_SHA
        run: |
          set -u
          echo "sha=$GITHUB_SHA"
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
| 1 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---