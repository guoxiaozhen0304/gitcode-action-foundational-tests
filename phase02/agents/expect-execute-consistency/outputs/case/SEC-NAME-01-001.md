# SEC-NAME-01-001
- **标题**: Secret/变量名含特殊字符时不可导致意外求值或权限绕过   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
含中划线的secret(MY-VAR)不应因解析错误被泄露，或不支持时应在YAML校验阶段报错。
## 做了什么
YAML workflow使用${{ secrets.MY-VAR }}。断言含must_not_contain_secret和success_or_yaml_error(兼容两种预期路径)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "MY-VAR" | COVERED | 日志搜索secret原值 |
| 2 | run_status | positive | equals "success_or_yaml_error" | COVERED | 成功或校验错误均为可接受的预期路径 |
