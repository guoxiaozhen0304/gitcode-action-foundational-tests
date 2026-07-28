# COMP-BOUND-01-085

- **标题**: cron 表达式格式与位置边界验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 schedule cron 表达式支持 `*` 任意值、`,` 列表、`-` 范围、`/` 步长，五段式格式正确。

## 做了什么
workflow 声明三条合法 cron；step 内运行 `python3` 脚本解析 cron 字符串，按 5 段式 + 字符集合法性校验后逐条输出 `CRON_VALID=<expr> True`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 三条合法 cron 通过平台注册且 workflow 执行成功 |
| 2 | run_logs | positive | must_contain: CRON_VALID=*/5 * * * * True | COVERED | python3 脚本正则校验后 print 输出 |
| 3 | run_logs | positive | must_contain: CRON_VALID=0 2,14 * * * True | COVERED | 同上 |
| 4 | run_logs | positive | must_contain: CRON_VALID=0 9-17 * * 1-5 True | COVERED | 同上 |
