# COMP-SUMMARY-01-001

- **标题**: ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-018

通过标准：
1. type=positive, target=step_summary, contains="Test Summary"
2. type=positive, target=step_summary_html, contains="<table>"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write summary | `echo "## Test Summary" >> "$ATOMGIT_STEP_SUMMARY" echo "| Metric | Value |" >> "` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step summary rendering
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write summary
        run: |
          echo "## Test Summary" >> "$ATOMGIT_STEP_SUMMARY"
          echo "| Metric | Value |" >> "$ATOMGIT_STEP_SUMMARY"
          echo "|---|---|" >> "$ATOMGIT_STEP_SUMMARY"
          echo "| Status | Pass |" >> "$ATOMGIT_STEP_SUMMARY"
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
| 1 | step_summary | positive | contains=Test Summary | ✅ GENUINE | 步骤有 step_summary 输出，断言可观测 |
| 2 | step_summary_html | positive | contains=<table> | ✅ GENUINE | 断言有条件可被步骤验证 |

---