# SEC-MASK-01-003
- **标题**: Secret 日志脱敏不可通过 base64 编码绕过   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
base64编码后的secret不应以明文形式出现在日志中，系统应能识别编码后secret并执行脱敏。
## 做了什么
YAML workflow中step对secret做base64编码后echo。第一个断言为must_not_contain_secret(机器判定)，第二个为llm_assisted(base64遮蔽判定)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 日志搜索secret明文为可机器判定 |
| 2 | run_logs | negative | base64编码后也应被遮蔽 | UNVERIFIABLE | eval:llm_assisted，base64字符串与secret的一一对应关系需LLM判定 |
