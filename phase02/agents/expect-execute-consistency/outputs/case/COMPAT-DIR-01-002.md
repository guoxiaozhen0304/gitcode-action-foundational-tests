# COMPAT-DIR-01-002

- **标题**: 工作流目录差异——.github/workflows/ 不应被识别
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**工作流目录差异——.github/workflows/ 不应被识别**

- 触发事件: `push`
- 规格引用: INTENT-COMPAT-029

通过标准：
1. type=negative, target=workflow_discovery, eval=llm_assisted
2. type=negative, target=run_logs, eval=llm_assisted
3. type=positive, target=run_status, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) echo if reached | `echo "GITHUB_DIR_WORKFLOW_RAN"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  verify-github-dir-ignored:
    name: Verify .github workflows dir ignored
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) echo if reached
        run: |
          echo "GITHUB_DIR_WORKFLOW_RAN"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-github-dir` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_discovery | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---