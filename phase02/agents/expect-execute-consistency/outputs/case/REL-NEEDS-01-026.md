# REL-NEEDS-01-026

- **标题**: needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行
- **维度**: 可靠性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-069

通过标准：
1. type=positive, target=job_b_status, equals=success
2. type=positive, target=job_a_status, equals=success
3. type=negative, target=job_a_status, equals=skipped
4. type=nonfunctional, target=downstream_start_delay_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | matrix work step | `echo "matrix_instance=${{ matrix.version }}"` |  | ✅ GENUINE |
| 2 | read needs result step | `echo "needs_result=${{ needs.job_b.result }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job_b:
    name: matrix upstream job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        version: [1, 2, 3]
      fail-fast: false
    steps:
      - name: matrix work step
        run: |
          echo "matrix_instance=${{ matrix.version }}"
  job_a:
    name: downstream aggregator job
    runs-on: [ubuntu-latest, x64, small]
    needs: job_b
    steps:
      - name: read needs result step
        run: |
          echo "needs_result=${{ needs.job_b.result }}"
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
| 1 | job_b_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | job_a_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | job_a_status | negative | equals=skipped | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | downstream_start_delay_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---