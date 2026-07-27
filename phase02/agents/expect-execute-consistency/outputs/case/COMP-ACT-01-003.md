# COMP-ACT-01-003

- **标题**: 手动取消时 action runs.post 由调度服务调用
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**手动取消时 action runs.post 由调度服务调用**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-028

通过标准：
1. type=positive, target=run_logs, must_contain="POST_CLEANUP_DONE"
2. type=negative, target=run_status, equals=success
3. type=nonfunctional, target=post_latency, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Run cancellable action | `./.gitcode/actions/post-hook` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  longrun:
    name: Long running job with post action
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run cancellable action
        uses: ./.gitcode/actions/post-hook
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `local-action-post` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=POST_CLEANUP_DONE | ✅ GENUINE | POST_CLEANUP_DONE: GENUINE (uses action 内部输出) |
| 2 | run_status | negative | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 3 | post_latency | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---