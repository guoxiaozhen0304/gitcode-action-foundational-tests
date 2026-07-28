# SEC-NAME-01-004
- **标题**: 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值
- **维度**: security
- **评级**: 断言一致

## 想测什么
job env 中声明与平台系统变量同名的 ATOMGIT_ENV 不应替换平台注入值。

## 做了什么
workflow 在 job env 中声明 ATOMGIT_ENV=/tmp/fixture-shadow-path；脚本比对实际取值与平台注入值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "SYSTEM_VAR_PRESERVED_OK" | COVERED | 对应"系统变量取值与平台注入值一致"；real script→GENUINE |
| 2 | run_logs | negative | must_not_contain "SYSTEM_VAR_SHADOWED_BAD" | COVERED | 对应"系统变量值绝不应被同名用户自定义值替换"；script判等→GENUINE |
