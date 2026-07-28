# USE-MASK-01-001
- **标题**: secret 脱敏文档描述与实际行为一致并给出缓解建议
- **维度**: 易用性/安全性
- **评级**: 部分不符

## 想测什么
验证通过 env 注入方式引用 secret 时，日志中 secret 值显示为 ***（原值不出现），同时检查文档是否给出可操作的缓解建议。

## 做了什么
workflow 在 env 层注入 TEST_SECRET，两个 step 分别输出 secret 长度和直接输出 secret 值。断言日志含 *** 且不含原值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 日志含 "***" | COVERED | 平台脱敏行为在日志中可观察 → GENUINE |
| 2 | run_logs | positive | 日志不含 TEST_SECRET 原值 | COVERED | must_not_contain_secret 可由 harness 字符串匹配判定 |
| 3 | documentation | nonfunctional | 文档风险提示含可操作建议 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
