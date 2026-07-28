# COMP-EXPR-01-058

- **标题**: 表达式运算符与优先级边界行为
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `==`、`!=`、`!`、`>`、`<`、`>=`、`<=`、`&&`、`||` 运算符及优先级组合的求值行为。

## 做了什么
多个 step 在 `if:` 条件中使用各运算符：`==`、`!=`（含负向不匹配）、`!`、`>`、`<`、`>=`、`<=`、`true && (false || true)`。实际运行上下文均为 `workflow_dispatch`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: eq_passed | COVERED | `atomgit.event_name == 'workflow_dispatch'` 为 true → 步骤执行 |
| 2 | run_logs | positive | must_contain: ne_passed | COVERED | `atomgit.ref_name != 'nonexistent'` 为 true → 步骤执行 |
| 3 | run_logs | positive | must_contain: not_passed | COVERED | `!false` 为 true → 步骤执行 |
| 4 | run_logs | positive | must_contain: gt_passed | COVERED | `5 > 3` 为 true → 步骤执行 |
| 5 | run_logs | positive | must_contain: lt_passed | COVERED | `2 < 3` 为 true → 步骤执行 |
| 6 | run_logs | positive | must_contain: ge_passed | COVERED | `3 >= 3` 为 true → 步骤执行 |
| 7 | run_logs | positive | must_contain: le_passed | COVERED | `3 <= 4` 为 true → 步骤执行 |
| 8 | run_logs | positive | must_contain: logic_passed | COVERED | `true && (false || true)` 优先级正确执行 |
| 9 | run_logs | negative | must_not_contain: eq_negative_unexpected | COVERED | `atomgit.event_name == 'push'` 为 false → 步骤不执行 |
