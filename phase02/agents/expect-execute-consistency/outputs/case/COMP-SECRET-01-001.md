# COMP-SECRET-01-001

- **标题**: echo secret 在日志中被脱敏为 ***
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `echo ${{ secrets.TEST_SECRET }}` 输出被脱敏为 ***。

## 做了什么
Step: `echo "secret is ${{ secrets.TEST_SECRET }}"`——使用 `${{ secrets.* }}` 表达式故意输出 secret 测试脱敏。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains "***" | COVERED | secret 被使用并输出，平台自动脱敏产生 `***`；真实安全测试（Rule 4） |
| 2 | run_logs | negative | must_not_contain_secret TEST_SECRET | COVERED | secret 经 ${{ secrets }} 使用，must_not_contain_secret 是真实安全断言（Rule 4） |
