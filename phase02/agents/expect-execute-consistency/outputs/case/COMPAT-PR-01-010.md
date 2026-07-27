# COMPAT-PR-01-010

- **标题**: 存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-039

通过标准：
1. type=negative, target=run_list, eval=llm_assisted
2. type=nonfunctional, target=run_list, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mark conflicted PR run | `echo "CONFLICT_PR_JOB_RAN"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
    types: [open, update]
jobs:
  probe:
    name: Probe merge conflict trigger policy
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mark conflicted PR run
        run: |
          echo "CONFLICT_PR_JOB_RAN"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-merge-conflict-pr` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_list | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---