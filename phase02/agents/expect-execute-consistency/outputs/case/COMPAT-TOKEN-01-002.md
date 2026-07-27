# COMPAT-TOKEN-01-002

- **标题**: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-020

通过标准：
1. type=negative, target=run_logs, eval=llm_assisted
2. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use GITHUB_TOKEN for API  | `STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test GITHUB_TOKEN unavailable
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use GITHUB_TOKEN for API call
        run: |
          STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}" -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}")
          echo "api_status=$STATUS"
          echo "done"
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
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---