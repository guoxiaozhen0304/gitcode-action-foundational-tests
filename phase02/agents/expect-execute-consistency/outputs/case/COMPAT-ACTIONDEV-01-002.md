# COMPAT-ACTIONDEV-01-002

- **标题**: action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-048

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=negative, target=run_logs, eval=llm_assisted
3. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Invoke local node16 actio | `./.gitcode/actions/probe-node16` |  | ✅ GENUINE |
| 2 | Invoke local composite ac | `./.gitcode/actions/probe-composite` |  | ✅ GENUINE |
| 3 | Invoke local docker actio | `./.gitcode/actions/probe-docker` |  | ✅ GENUINE |
| 4 | Invoke local node20 actio | `./.gitcode/actions/probe-node20` |  | ✅ GENUINE |
| 5 | Mark probe complete | `echo "USING_PROBE_DONE"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe runs using runtime coverage
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Invoke local node16 action
        uses: ./.gitcode/actions/probe-node16
      - name: Invoke local composite action
        uses: ./.gitcode/actions/probe-composite
      - name: Invoke local docker action
        uses: ./.gitcode/actions/probe-docker
      - name: Invoke local node20 action
        uses: ./.gitcode/actions/probe-node20
      - name: Mark probe complete
        run: |
          echo "USING_PROBE_DONE"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-local-actions` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---