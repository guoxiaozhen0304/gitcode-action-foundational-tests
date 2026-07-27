# USE-ANNOT-01-002

- 标题: ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转
- 维度: 易用性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   USE-ANNOT-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-021
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md
母意图:    —
标题:      ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转

前置条件:
  - PR 存在
  - workflow 由 PR 事件触发

操作步骤:
  1. 在 PR 触发的工作流中输出 ::error file=...,line=...::message
  2. 检查 PR 页面的 annotation 展示

预期结果:
  若支持 annotation，则 PR 页面显示包含文件路径、行号、错误信息的红色/黄色标注，且可点击跳转

验证点:
  - [非功能] annotation 是否包含准确的文件路径、行号、错误信息
  - [非功能] annotation 颜色是否符合语义（error 红色、warning 黄色）

清理:      无

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout | uses: checkout | 是 |
| 2 | emit annotation | run: echo "::error file=README.md,line=1::..." ; echo "::warning file=README.md,line=2::..." | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    types:
      - open
      - update
    branches: [main]
jobs:
  annot-pr:
    name: PR annotation test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout
        uses: checkout
      - name: emit annotation
        run: |
          echo "::error file=README.md,line=1::Test error annotation"
          echo "::warning file=README.md,line=2::Test warning annotation"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [非功能] annotation 是否包含准确的文件路径、行号、错误信息 | 🔄 UNVERIFIABLE | 断言 type=nonfunctional, eval=llm_assisted, target=pr_ui；annotation 的 UI 呈现（文件路径、行号、错误信息准确性）需 LLM 辅助评估 PR 页面，无法通过步骤输出直接判定 |
| [非功能] annotation 颜色是否符合语义（error 红色、warning 黄色） | 🔄 UNVERIFIABLE | 同上，颜色语义判断依赖 UI 截图/页面渲染，步骤自身无法产出可对比的断言结果 |

### 问题

- **两个验证点均为 UNVERIFIABLE**：断言类型为 nonfunctional，评估方式为 llm_assisted，目标为 pr_ui。workflow 步骤仅通过 echo 向日志输出 `::error` / `::warning` 工作流命令字符串，是否真正在 PR 页面生成 annotation、路径/行号/颜色是否正确，均无法通过步骤日志直接验证，必须依赖 LLM 审查 PR UI。

## 5. 评级理由

YAML 中唯一的断言为 `type: nonfunctional, target: pr_ui, eval: llm_assisted`。两个规格验证点均属于非功能性 UI 验证，依赖 LLM 辅助评估 annotation 在 PR 页面的呈现效果。步骤自身无法产出这些断言所需的可观测输出，因此均为 UNVERIFIABLE。
