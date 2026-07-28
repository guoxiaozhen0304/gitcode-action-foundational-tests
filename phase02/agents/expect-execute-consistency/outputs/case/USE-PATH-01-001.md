# USE-PATH-01-001  - **标题**: paths 300 文件上限在文档与行为中一致且明示   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

文档在显眼位置标注 300 文件上限；超出时调试日志有提示

## 做了什么

- 1. 检查 configure-triggers.md 中 paths 说明
- 2. 触发一次变更文件数超过 300 的 push

- - [非功能] 文档 paths 章节顶部或注意块中是否有 300 文件上限提示
- - [非功能] 超出上限时调试日志是否提示 paths 过滤超出文件上限

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 文档paths说明位置与内容需LLM评估 |
