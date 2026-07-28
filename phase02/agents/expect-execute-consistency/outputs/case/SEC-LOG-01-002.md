# SEC-LOG-01-002
- **标题**: 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
所有日志副本(含导出件)中secret原值命中数为0，历史日志遮蔽状态不随后续操作回退。
## 做了什么
YAML workflow中step echo ${{ secrets.DEPLOY_TOKEN }}产生日志。断言target exported_logs和历史日志historical_logs，均为workflow运行后的衍生品。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | log_api | positive | equals "download_ok" | COVERED | 日志可下载为可观测行为 |
| 2 | exported_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 导出日志全文搜索secret为确定性可观测操作 |
| 3 | historical_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 历史日志同样可全文搜索判定 |
