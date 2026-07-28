# SEC-LOG-01-002
- **标题**: 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补规格中"遮蔽状态不可回退"验证点的对应断言（negative mask_regression_detected）。原 3 条断言本已 COVERED。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_api | positive | equals download_ok | ✅ COVERED | 日志可下载 |
| 2 | exported_logs | negative | must_not_contain_secret DEPLOY_TOKEN | ✅ GENUINE | 导出日志全文检索原值 |
| 3 | historical_logs | negative | must_not_contain_secret DEPLOY_TOKEN | ✅ GENUINE | 历史日志全文检索原值 |
| 4 | mask_regression_detected | negative | equals true | ✅ COVERED | 负向：遮蔽不得回退 |
