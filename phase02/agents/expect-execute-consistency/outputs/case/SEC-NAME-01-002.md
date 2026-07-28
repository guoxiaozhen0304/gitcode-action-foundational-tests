# SEC-NAME-01-002
- **标题**: 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏
- **维度**: security
- **评级**: 断言一致

## 想测什么
printenv/proc/environ 输出日志时 secret 值被脱敏；未以环境变量暴露时输出 not found。

## 做了什么
workflow printenv | grep API_KEY 和 cat /proc/self/environ | grep API_KEY。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 对应"printenv 输出到日志时 secret 值必须被脱敏"；platform→GENUINE |
| 2 | run_logs | positive | contains "not found" | COVERED | 对应"secret 未以环境变量暴露时输出 not found"；real cmd→GENUINE |
