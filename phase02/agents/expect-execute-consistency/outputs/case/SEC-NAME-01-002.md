# SEC-NAME-01-002
- **标题**: 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
printenv或读取/proc/self/environ输出到日志时secret值必须被脱敏；若secret未暴露则输出not found。
## 做了什么
YAML workflow中两个step分别执行printenv | grep API_KEY 和 cat /proc/self/environ | grep API_KEY，均fallback输出"not found"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 日志全文搜索secret原值 |
| 2 | run_logs | positive | contains "not found" | COVERED | 输出为workflow step的直接产物 |
