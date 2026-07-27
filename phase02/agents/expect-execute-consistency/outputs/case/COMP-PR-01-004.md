# COMP-PR-01-004

- **标题**: pre-merge ref 在 PR 存续期可解析且语义裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pre-merge ref 在 PR 存续期可解析且语义裁定**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-033

通过标准：
1. type=positive, target=run_logs, must_contain="PRE_MERGE_MARKER"
2. type=positive, target=run_logs, must_contain="REF_CONTENT_DUMPED"
3. type=nonfunctional, target=ref_semantics, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Checkout merge ref | `checkout` |  | ✅ GENUINE |
| 2 | Inspect content | `cat pre_merge_marker.txt echo "REF_CONTENT_DUMPED"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  checkoutmerge:
    name: Checkout pre merge ref
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout merge ref
        uses: checkout
        with:
          ref: refs/merge-requests/1/merge
      - name: Inspect content
        run: |
          cat pre_merge_marker.txt
          echo "REF_CONTENT_DUMPED"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `maintainer` |
| Repo 环境 | `pr-merge-ref` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=PRE_MERGE_MARKER | ✅ GENUINE | PRE_MERGE_MARKER: GENUINE (uses action 内部输出) |
| 2 | run_logs | positive | must_contain=REF_CONTENT_DUMPED | ✅ GENUINE | REF_CONTENT_DUMPED: GENUINE |
| 3 | ref_semantics | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---