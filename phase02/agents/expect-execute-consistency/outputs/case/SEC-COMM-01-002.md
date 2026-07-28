# SEC-COMM-01-002
- **标题**: 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发
- **维度**: security
- **评级**: 断言一致

## 想测什么
精确指令评论正常触发，引用/反讽/代码块内嵌指令文本不触发。

## 做了什么
workflow 配置 comments: ['^/deploy fixture-environment$'] 锚定正则；harness 分批发边界评论与精确指令。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_trigger | positive | equals "exact_command_triggers" | COVERED | 对应"符合配置意图的精确指令评论正常触发"；COVERED |
| 2 | run_trigger | negative | must_not_equal "triggered_by_quoted_or_embedded_text" | COVERED | 对应"引用/反讽/代码块内嵌指令文本绝不应造成预期外触发"；COVERED |
| 3 | trigger_audit | nonfunctional | eval llm_assisted | COVERED | 对应"每次触发可回溯到具体评论内容"；LLM 辅助 = 断言一致 |
