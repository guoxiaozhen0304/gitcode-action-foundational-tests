# REL-MATRIXFAIR-01-056

- **标题**: 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-056

通过标准：
1. type=positive, target=completed_jobs_count, equals=20
2. type=nonfunctional, target=queued_delay_ratio

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | matrix step | `echo version=${{ matrix.version }}` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: matrix test job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        version: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
      max-parallel: 4
    steps:
      - name: matrix step
        run: |
          echo version=${{ matrix.version }}
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
| 1 | completed_jobs_count | positive | equals=20 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | queued_delay_ratio | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---