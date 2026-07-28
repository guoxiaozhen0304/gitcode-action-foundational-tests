# COMP-BOUND-01-085
- **标题**: cron 表达式格式与位置边界验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
cron 五段式格式正确，支持 * 任意值、, 列表、- 范围与 / 步长，分钟/小时/日/月/星期位置正确。

## 做了什么
1. step `Validate cron expressions`：python3 脚本正则解析三条 cron（"*/5 * * * *"、"0 2,14 * * *"、"0 9-17 * * 1-5"），逐条输出 CRON_VALID= 结果
2. trigger.event: schedule

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | python3 脚本执行是真实命令 |
| 2 | run_logs | positive | must_contain: CRON_VALID=*/5 * * * * True | COVERED | python3 print 直接输出 |
| 3 | run_logs | positive | must_contain: CRON_VALID=0 2,14 * * * True | COVERED | python3 print 直接输出 |
| 4 | run_logs | positive | must_contain: CRON_VALID=0 9-17 * * 1-5 True | COVERED | python3 print 直接输出 |
