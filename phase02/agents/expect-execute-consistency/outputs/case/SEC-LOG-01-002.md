# SEC-LOG-01-002
- **标题**: 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退
- **维度**: security
- **评级**: 断言一致

## 想测什么
所有日志副本中 secret 原值命中数为0；历史日志遮蔽不随操作回退。

## 做了什么
workflow echo secrets.DEPLOY_TOKEN；harness 对导出/历史日志检查遮蔽状态。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_api | positive | equals "download_ok" | COVERED | 对应"日志可正常下载导出" |
| 2 | exported_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"导出件中 secret 原值命中数为 0"；harness→GENUINE |
| 3 | historical_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 对应"历史日志中 secret 原值命中数为 0"；harness→GENUINE |
| 4 | mask_regression_detected | negative | equals "true" | COVERED | 对应"遮蔽状态不可回退"；negative + equals true = "不应发生" |
