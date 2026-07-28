# SEC-MASK-01-006
- **标题**: Secret 日志脱敏不可通过分片输出绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
逐字符分片输出 secret 时各片段被脱敏，或分片到不可还原长度以下。

## 做了什么
workflow for 循环逐字符 echo secret；明文由 must_not_contain_secret 覆盖，子串由 llm_assisted。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 完整原值确定性覆盖 |
| 2 | run_logs | negative | eval llm_assisted | COVERED | 对应"分片输出不应保留明文"；子串阈值动态→LLM 辅助 = 断言一致 |
