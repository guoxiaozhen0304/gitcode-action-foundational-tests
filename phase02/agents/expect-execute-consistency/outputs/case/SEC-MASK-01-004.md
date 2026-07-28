# SEC-MASK-01-004
- **标题**: Secret 日志脱敏不可通过字符串拼接或插值绕过   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
拼接后的secret值不应以可还原形式出现在日志中，分多行输出也应保持脱敏。
## 做了什么
YAML workflow将secret分两段(cut -c1-4和cut -c5-8)拼接输出。第二个断言为llm_assisted子串检查。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 明文原值搜索可机器判定 |
| 2 | run_logs | negative | 任意连续子串命中数为0 | UNVERIFIABLE | eval:llm_assisted，子串长度阈值判定需LLM辅助 |
