# USE-PATH-01-001
- **标题**: paths 300 文件上限在文档与行为中一致且明示
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
检查文档 configure-triggers.md 中 paths/paths-ignore 说明是否在显眼位置标注 300 文件匹配上限。

## 做了什么
纯文档检查用例（workflow: null）。检查文档路径说明中是否说明了匹配前 300 个变更文件的上限。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | nonfunctional | 文档在 paths 说明首段或注意块中写明 300 文件上限 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
