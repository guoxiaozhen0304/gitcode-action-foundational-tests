# SEC-MASK-01-004
- **标题**: Secret 日志脱敏不可通过字符串拼接或插值绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
secret 拆分拼接后输出到日志，不应以可还原形式出现。

## 做了什么
workflow 对 secret 做 cut 分片后拼接 echo；明文由 must_not_contain_secret 覆盖，子串由 llm_assisted。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 完整原值确定性覆盖 |
| 2 | run_logs | negative | eval llm_assisted | COVERED | 对应"拼接后不应以可还原形式出现"；子串阈值动态→LLM 辅助 = 断言一致 |
