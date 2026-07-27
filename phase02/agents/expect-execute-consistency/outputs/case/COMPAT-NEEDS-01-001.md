# COMPAT-NEEDS-01-001

- **标题**: needs 上下文存在性与 outputs/result 字段对齐（规格矛盾仲裁）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**needs 上下文存在性与 outputs/result 字段对齐（规格矛盾仲裁）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-041

通过标准：
1. type=positive, target=run_logs, must_contain="NEEDS_VERSION=1.2.3"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Generate version output | `echo "version=1.2.3" >> "$ATOMGIT_OUTPUT"` |  | ❌ VACUOUS |
| 2 | Read needs outputs and re | `echo "NEEDS_VERSION=${{ needs.build.outputs.version }}" echo "NEEDS_RESULT=${{ n` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  build:
    name: Produce version output
    runs-on: [ubuntu-latest, x64, small]
    outputs:
      version: ${{ steps.gen.outputs.version }}
    steps:
      - name: Generate version output
        id: gen
        run: |
          echo "version=1.2.3" >> "$ATOMGIT_OUTPUT"
  consume:
    name: Consume needs context
    needs: build
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Read needs outputs and result
        run: |
          echo "NEEDS_VERSION=${{ needs.build.outputs.version }}"
          echo "NEEDS_RESULT=${{ needs.build.result }}"
          echo "PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=NEEDS_VERSION=1.2.3 | ❌ MISSING_SOURCE | NEEDS_VERSION=1.2.3: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — MISSING_SOURCE**❌: NEEDS_VERSION=1.2.3: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---