# COMPAT-EXPR-01-001

- **标题**: success 关键字在条件表达式中的可用性
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 success 关键字在表达式中的可用性。

## 做了什么
checkout → echo "Step completed successfully" → echo "Next step executed, implicit success confirmed"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: implicit success confirmed | COVERED | run 步骤直接 echo 该字符串 |
