# COMP-TRIG-01-072

- **标题**: push 事件关键字段与过滤验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 push 事件的 ref、before、after 等关键字段可访问。

## 做了什么
Steps: `echo "REF=${{ atomgit.event.ref }}"`、`echo "BEFORE=${{ atomgit.event.before }}"`、`echo "AFTER=${{ atomgit.event.after }}"`——均使用 `${{ }}` 表达式。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain REF=refs/ | COVERED | step 含 `${{ atomgit.event.ref }}` 上下文表达式（Rule 6） |
| 2 | run_logs | positive | must_contain BEFORE= | COVERED | step 含 `${{ atomgit.event.before }}` 表达式 |
| 3 | run_logs | positive | must_contain push_ok | COVERED | marker signal: all event fields accessible |
