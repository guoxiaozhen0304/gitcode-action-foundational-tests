# COMPAT-MATRIX-01-005

- **标题**: matrix exclude 全排除不被支持时的差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**matrix exclude 全排除不被支持时的差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-007

通过标准：
1. type=positive, target=validation_error, eval=llm_assisted
2. type=negative, target=run_status, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo matrix values | `echo "os=${{ matrix.os }}" echo "node=${{ matrix.node }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-matrix-exclude:
    name: Test matrix exclude all
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        os: [ubuntu]
        node: [16]
        exclude:
          - os: ubuntu
            node: 16
    steps:
      - name: Echo matrix values
        run: |
          echo "os=${{ matrix.os }}"
          echo "node=${{ matrix.node }}"
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
| 1 | validation_error | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_status | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---