# COMPAT-LIMIT-01-002

- **标题**: workflow_dispatch 输入数量上限（GitHub 25 个）与非默认分支可用性
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**workflow_dispatch 输入数量上限（GitHub 25 个）与非默认分支可用性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-052

通过标准：
1. type=positive, target=save_result, eval=llm_assisted
2. type=negative, target=save_result, eval=llm_assisted
3. type=positive, target=run_list, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mark dispatch run | `echo "DISPATCH_LIMIT_PROBE_RAN"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      in01: {description: probe, required: false}
      in02: {description: probe, required: false}
      in03: {description: probe, required: false}
      in04: {description: probe, required: false}
      in05: {description: probe, required: false}
      in06: {description: probe, required: false}
      in07: {description: probe, required: false}
      in08: {description: probe, required: false}
      in09: {description: probe, required: false}
      in10: {description: probe, required: false}
      in11: {description: probe, required: false}
      in12: {description: probe, required: false}
      in13: {description: probe, required: false}
      in14: {description: probe, required: false}
      in15: {description: probe, required: false}
      in16: {description: probe, required: false}
      in17: {description: probe, required: false}
      in18: {description: probe, required: false}
      in19: {description: probe, required: false}
      in20: {description: probe, required: false}
      in21: {description: probe, required: false}
      in22: {description: probe, required: false}
      in23: {description: probe, required: false}
      in24: {description: probe, required: false}
      in25: {description: probe, required: false}
      in26: {description: probe, required: false}
jobs:
  probe:
    name: Probe dispatch inputs limit
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mark dispatch run
        run: |
          echo "DISPATCH_LIMIT_PROBE_RAN"
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
| 1 | save_result | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | save_result | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_list | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---