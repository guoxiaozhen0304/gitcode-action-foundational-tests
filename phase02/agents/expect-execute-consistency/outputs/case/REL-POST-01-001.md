# REL-POST-01-001
- **标题**: post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 GitCode 特有 post 阶段的失败语义：主 steps 成功 + post 失败时 conclusion 归因正确；主 step 失败时 post（run_always）仍执行；post 不 hang 超时。
## 做了什么
3 组变体：a) 主 steps 成功 + post 失败（exit 1）；b) 主 step 失败 + post 正常；c) post 内超时。harness 按组注入变体。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | conclusion_matches_documented_semantics | positive | equals "true" | COVERED | harness 比对 conclusion 与文档声明语义 |
| 2 | post_failure_attribution_visible | positive | equals "true" | COVERED | harness 解析日志确认 post 失败归因明确 |
| 3 | silent_post_swallow_detected | negative | equals "true" | COVERED | harness 检测 post 静默吞掉失败的场景 |
| 4 | post_hang_beyond_timeout_detected | negative | equals "true" | COVERED | harness 检测 post 阶段 hang 超过 timeout 的场景 |
