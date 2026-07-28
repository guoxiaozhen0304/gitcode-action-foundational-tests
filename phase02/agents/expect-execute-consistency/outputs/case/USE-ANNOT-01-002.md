# USE-ANNOT-01-002
- **标题**: ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
若支持 annotation，PR 页面显示包含文件路径、行号、错误信息的标注且可点击跳转。

## 做了什么
workflow 以 pull_request 触发，通过 `echo "::error file=README.md,line=1::Test error annotation"` 生成 annotation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | pr_ui | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定 PR 页面 annotation 是否包含准确的文件路径、行号、颜色语义 |

