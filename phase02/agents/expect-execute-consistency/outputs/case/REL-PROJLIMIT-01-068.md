# REL-PROJLIMIT-01-068

- **标题**: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-068

通过标准：
1. type=positive, target=completed_count, equals=201
2. type=positive, target=failed_count, equals=0
3. type=positive, target=queued_count
4. type=nonfunctional, target=total_duration_seconds
5. type=nonfunctional, target=lost_count, equals=0

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | quick step | `echo "run_id=${{ atomgit.run_id }}" sleep 5` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: concurrency limit boundary job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: quick step
        run: |
          echo "run_id=${{ atomgit.run_id }}"
          sleep 5
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
| 1 | completed_count | positive | equals=201 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | failed_count | positive | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | queued_count | positive |  | ✅ GENUINE | 通用断言匹配 |
| 4 | total_duration_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 5 | lost_count | nonfunctional | equals=0 | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 5 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---