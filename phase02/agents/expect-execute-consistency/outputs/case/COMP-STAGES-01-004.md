# COMP-STAGES-01-004

- **标题**: map 形式 stages 按定义顺序串行执行（回归保护）
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**map 形式 stages 按定义顺序串行执行（回归保护）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-019

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, must_contain="STAGE_ONE_DONE"
3. type=positive, target=run_logs, must_contain="STAGE_TWO_DONE"
4. type=nonfunctional, target=stage_order, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
stages:
  build_stage:
    jobs:
      build:
        name: Stage one job
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Mark stage one
            run: |
              echo "STAGE_ONE_DONE"
  test_stage:
    jobs:
      test:
        name: Stage two job
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Mark stage two
            run: |
              echo "STAGE_TWO_DONE"
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
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | run_logs | positive | must_contain=STAGE_ONE_DONE | ❌ MISSING_SOURCE | STAGE_ONE_DONE: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=STAGE_TWO_DONE | ❌ MISSING_SOURCE | STAGE_TWO_DONE: MISSING_SOURCE (无步骤产出此字符串) |
| 4 | stage_order | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

**断言 2 — MISSING_SOURCE**❌: STAGE_ONE_DONE: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — MISSING_SOURCE**❌: STAGE_TWO_DONE: MISSING_SOURCE (无步骤产出此字符串)

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---