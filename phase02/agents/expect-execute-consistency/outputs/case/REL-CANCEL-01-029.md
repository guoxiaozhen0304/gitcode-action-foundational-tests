# REL-CANCEL-01-029

- **标题**: 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-070

通过标准：
1. type=positive, target=target_run_status, equals=canceled
2. type=positive, target=sibling_run_status, equals=success
3. type=negative, target=sibling_run_status, equals=canceled
4. type=nonfunctional, target=cancel_convergence_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | long sleep step | `sleep 300` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: cancel target correctness job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: long sleep step
        run: |
          sleep 300
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
| 1 | target_run_status | positive | equals=canceled | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | sibling_run_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | sibling_run_status | negative | equals=canceled | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | cancel_convergence_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---