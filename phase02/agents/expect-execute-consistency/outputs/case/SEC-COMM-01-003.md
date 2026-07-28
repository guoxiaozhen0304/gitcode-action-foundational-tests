# SEC-COMM-01-003
- **标题**: 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
变形评论（大小写变形、多余空白、markdown包裹）不应绕过comments过滤语义，文档应说明匹配规则。
## 做了什么
YAML workflow包含comments过滤和echo步骤。trigger为pull_request_comment，params含obfuscated_comments列表。第三个断言为llm_assisted文档检查。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_trigger | positive | equals "exact_command_triggers" | COVERED | 精确指令可触发，通过run状态判定 |
| 2 | run_trigger | negative | must_not_equal "triggered_by_obfuscated_variant" | COVERED | 变形评论不应触发，通过run状态判定 |
| 3 | documentation | nonfunctional | 文档应说明匹配语义与误触发警示 | UNVERIFIABLE | eval:llm_assisted，依赖LLM判定文档质量 |
