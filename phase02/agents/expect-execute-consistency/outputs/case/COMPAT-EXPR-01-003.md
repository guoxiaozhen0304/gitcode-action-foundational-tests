# COMPAT-EXPR-01-003

- **标题**: failure() 与 failed 关键字的处理行为差异
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 failure() 语义——force failure step 执行后，always() 条件下的 cleanup step 正常执行。

## 做了什么
checkout → exit 1 → cleanup (if: ${{ always() }}) echo "Cleanup ran after failure"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: Cleanup ran after failure | COVERED | always() 条件下 echo，exit 1 不阻断后续 |
| 2 | run_status | positive | equals: failure | COVERED | force failure step exit 1 导致失败 |
