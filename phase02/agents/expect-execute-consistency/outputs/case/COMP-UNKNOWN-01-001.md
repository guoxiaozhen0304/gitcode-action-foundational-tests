# COMP-UNKNOWN-01-001

- **标题**: 包含未知顶层字段的 workflow 触发 YAML 校验失败
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**包含未知顶层字段的 workflow 触发 YAML 校验失败**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-002

通过标准：
1. type=positive, target=run_status, equals=validation_failed
2. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo step | `echo "should not run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
unknown_field: true
on:
  workflow_dispatch:
jobs:
  test:
    name: Test unknown field
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo step
        run: |
          echo "should not run"
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
| 1 | run_status | positive | equals=validation_failed | ✅ GENUINE | 状态断言 validation_failed 可被步骤行为验证 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---