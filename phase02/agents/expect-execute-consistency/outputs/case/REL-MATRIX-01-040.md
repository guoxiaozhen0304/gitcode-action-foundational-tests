# REL-MATRIX-01-040

- **标题**: matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-076

通过标准：
1. type=positive, target=jobs_expanded_count, equals=256_or_explicit_rejection
2. type=negative, target=silent_truncation_detected, equals=true
3. type=nonfunctional, target=expand_enqueue_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | combo marker step | `echo "combo=${{ matrix.os }}-${{ matrix.ver }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: matrix 256 boundary job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        os: [os01, os02, os03, os04, os05, os06, os07, os08]
        ver: [v01, v02, v03, v04, v05, v06, v07, v08, v09, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32]
      fail-fast: false
      max-parallel: 5
    steps:
      - name: combo marker step
        run: |
          echo "combo=${{ matrix.os }}-${{ matrix.ver }}"
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
| 1 | jobs_expanded_count | positive | equals=256_or_explicit_rejection | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | silent_truncation_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | expand_enqueue_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---