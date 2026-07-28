# SEC-MASK-01-006
- **标题**: Secret 日志脱敏不可通过分片输出绕过   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
逐字符分片输出的secret各片段仍应被脱敏或分片至不可还原长度以下。
## 做了什么
YAML workflow中逐字符输出secret(loop for char)。第二个断言为llm_assisted子串检查(3字符以上连续子串命中数应为0)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 明文原值搜索可机器判定 |
| 2 | run_logs | negative | 3字符以上连续子串命中数应为0 | UNVERIFIABLE | eval:llm_assisted，连续子串判定需LLM辅助 |
