# SEC-COMM-01-003
- **标题**: 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义
- **维度**: security
- **评级**: 断言一致

## 想测什么
变形评论（大小写/空白/markdown包裹）不绕过过滤；精确指令正常触发。

## 做了什么
workflow 配置 comments: ['^/deploy fixture-environment$']；harness 分发变形评论。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_trigger | positive | equals "exact_command_triggers" | COVERED | 对应"未变形的精确指令评论正常触发" |
| 2 | run_trigger | negative | must_not_equal "triggered_by_obfuscated_variant" | COVERED | 对应"绕过过滤语义的伪装评论绝不应触发" |
| 3 | documentation | nonfunctional | eval llm_assisted | COVERED | 对应"匹配语义与误触发面有文档化说明"；LLM 辅助 = 断言一致 |
