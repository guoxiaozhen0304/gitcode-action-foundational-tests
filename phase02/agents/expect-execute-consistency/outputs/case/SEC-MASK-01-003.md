# SEC-MASK-01-003
- **标题**: Secret 日志脱敏不可通过 base64 编码绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
base64 编码后的 secret 值不应以明文出现在日志中。

## 做了什么
workflow 对 secret 做 base64 编码后 echo；明文由 must_not_contain_secret 覆盖，编码形式由 llm_assisted。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"日志中绝不应出现 DEPLOY_TOKEN 原值"；确定性覆盖 |
| 2 | run_logs | negative | eval llm_assisted | COVERED | 对应"base64 编码后仍应被遮蔽"；动态值→LLM 辅助 = 断言一致 |
