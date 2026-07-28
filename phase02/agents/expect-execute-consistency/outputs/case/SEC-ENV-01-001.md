# SEC-ENV-01-001
- **标题**: 环境级 secret 必须经审批后才能被 workflow 访问
- **维度**: security
- **评级**: 断言一致

## 想测什么
审批后 secret 可正常引用；审批前不可读取。

## 做了什么
workflow 引用 environment: production 的环境级 secret PROD_TOKEN；断言审批后成功、日志不泄露原值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "success_after_approval" | COVERED | 对应"审批后 secret 可被正常引用，job 成功执行" |
| 2 | run_logs | negative | must_not_contain_secret "PROD_TOKEN" | COVERED | 对应"workflow 无法读取到环境 secret 的值"→secret masking; platform→GENUINE |
