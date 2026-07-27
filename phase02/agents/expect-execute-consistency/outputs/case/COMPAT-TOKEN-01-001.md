# COMPAT-TOKEN-01-001

- **标题**: ATOMGIT_TOKEN 应正确返回有效令牌
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**ATOMGIT_TOKEN 应正确返回有效令牌**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-020

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, must_not_contain_secret="ATOMGIT_TOKEN"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use ATOMGIT_TOKEN for API | `STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test ATOMGIT_TOKEN availability
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use ATOMGIT_TOKEN for API call
        run: |
          STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}" -H "Authorization: token $ATOMGIT_TOKEN")
          echo "api_status=$STATUS"
          echo "done"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `['ATOMGIT_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | !secret=ATOMGIT_TOKEN | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 ATOMGIT_TOKEN |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 ATOMGIT_TOKEN

---