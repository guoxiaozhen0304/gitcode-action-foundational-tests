# COMP-UNKNOWN-01-002

- **标题**: 不应静默忽略未知字段导致用户误以为配置生效
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证平台不应静默忽略未知字段而继续执行。

## 做了什么
合法 workflow（无未知字段），step: `echo "should not run"`。断言目标为 harness 侧验证：当 workflow 含 unknown 字段时 run_status 不应为 success。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success_with_unknown_field_silently_ignored | COVERED | harness 在有 unknown 字段时检查 run_status，负向断言（platform validation case） |
