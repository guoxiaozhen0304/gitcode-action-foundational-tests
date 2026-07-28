# USE-ANNOT-01-002
- **标题**: ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转
- **维度**: usability
- **评级**: 断言一致

## 想测什么
PR 页面 annotation 应包含准确的文件路径、行号、错误信息，颜色符合语义。

## 做了什么
step uses:checkout + echo ::error:: 和 ::warning:: 注解命令。断言指向 pr_ui，LLM 辅助评估。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | pr_ui | nonfunctional | eval:llm_assisted | LLM_DEPENDENT | nonfunctional + llm_assisted 判定 UI annotation 渲染质量 |
