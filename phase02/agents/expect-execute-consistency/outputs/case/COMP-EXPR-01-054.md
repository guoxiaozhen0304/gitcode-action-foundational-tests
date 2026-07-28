# COMP-EXPR-01-054

- **标题**: 字符串函数 contains startsWith endsWith 边界行为
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `contains`、`startsWith`、`endsWith` 字符串函数在匹配/不匹配/大小写场景下的行为。

## 做了什么
step 在 `if:` 条件中使用 `${{ contains(atomgit.ref_name, 'main') }}`、`${{ startsWith(atomgit.ref, 'refs/heads/') }}`、`${{ endsWith(atomgit.ref_name, 'ain') }}`；step 在 run 中 echo `${{ contains('main', 'MAIN') }}`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: contains_passed | COVERED | contains 条件为 true，步骤执行并 echo 输出 |
| 2 | run_logs | positive | must_contain: startswith_passed | COVERED | startsWith 条件为 true，步骤执行并 echo 输出 |
| 3 | run_logs | positive | must_contain: endswith_passed | COVERED | endsWith 条件为 true，步骤执行并 echo 输出 |
| 4 | run_logs | positive | must_contain: CASE_MATCH=false | COVERED | `${{ contains('main', 'MAIN') }}` 区分大小写，返回 false |
