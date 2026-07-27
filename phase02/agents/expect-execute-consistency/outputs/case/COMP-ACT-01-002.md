# COMP-ACT-01-002

- **标题**: 含连字符 input_id 的 INPUT_ 环境变量命名裁定
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**含连字符 input_id 的 INPUT_ 环境变量命名裁定**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-027

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, must_contain="INPUT_DRY"
3. type=nonfunctional, target=env_naming, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Call with hyphenated inpu | `./.gitcode/actions/hyphen-input` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  callaction:
    name: Call action with hyphen input
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Call with hyphenated input
        uses: ./.gitcode/actions/hyphen-input
        with:
          dry-run: "yes"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `local-action-hyphen` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | must_contain=INPUT_DRY | ✅ GENUINE | INPUT_DRY: GENUINE (uses action 内部输出) |
| 3 | env_naming | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---