# SEC-NAME-01-001
- **标题**: Secret/变量名含特殊字符时不可导致意外求值或权限绕过
- **维度**: security
- **评级**: 断言一致

## 想测什么
含中划线的 secret MY-VAR 引用不应因解析错误泄露；不支持时应在校验阶段报错。

## 做了什么
workflow 引用 secrets.MY-VAR（含中划线）并 echo。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "MY-VAR" | COVERED | 对应"含中划线 secret 绝不应因解析错误被泄露"；platform→GENUINE |
| 2 | run_status | positive | equals "success_or_yaml_error" | COVERED | 对应"若不支持中划线应在 YAML 校验阶段报错"；trigger-dispatchable→COVERED |
