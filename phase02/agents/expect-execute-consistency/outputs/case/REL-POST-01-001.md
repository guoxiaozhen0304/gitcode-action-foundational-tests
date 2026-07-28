# REL-POST-01-001
- **标题**: post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
三组变体验证：post失败时conclusion与文档一致+归因post阶段；主step失败时post(run_always)仍执行；post不hang、超时收敛。

## 做了什么
主job success，post阶段exit 1。harness按组注入失败/超时变体。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | conclusion_matches_documented_semantics | positive | equals=true | COVERED | 文本"post失败时conclusion与文档语义一致，日志归因post阶段"对应 |
| 2 | post_failure_attribution_visible | positive | equals=true | COVERED | 文本"日志明确归因post阶段"对应 |
| 3 | silent_post_swallow_detected | negative | equals=true | COVERED | 文本"不应post失败无任何标注而conclusion=success(静默吞掉)"精确对应 |
| 4 | post_hang_beyond_timeout_detected | negative | equals=true | COVERED | 文本"不应post阶段hang导致超过timeout仍不收敛"精确对应 |
