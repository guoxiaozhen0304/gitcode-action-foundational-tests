# COMP-TRIG-01-075

- **标题**: schedule 事件关键字段与 cron 格式验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 schedule 事件 schedule 字段可访问，数组格式通过校验。

## 做了什么
Step: `echo "SCHEDULE=${{ atomgit.event.schedule }}"`——`${{ }}` 表达式。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain schedule_ok | COVERED | step 含 `${{ atomgit.event.schedule }}` 上下文表达式（Rule 6） |
