# COMPAT-COMM-01-001

- **标题**: issue_comment types 命名差异 - GitCode 合法 types 应被接受
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**issue_comment types 命名差异 - GitCode 合法 types 应被接受**

- 触发事件: `issue_comment`
- 规格引用: INTENT-COMPAT-NEW-004

通过标准：
1. type=positive, target=run_status, equals=success, eval=llm_assisted
2. type=negative, target=validation_error, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo trigger info | `echo "event_name=${{ atomgit.event_name }}" echo "done"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created, edited]
jobs:
  test-comment-types:
    name: Test issue comment types
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo trigger info
        run: |
          echo "event_name=${{ atomgit.event_name }}"
          echo "done"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `issue_comment` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | validation_error | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---