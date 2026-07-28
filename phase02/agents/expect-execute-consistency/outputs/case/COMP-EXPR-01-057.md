# COMP-EXPR-01-057

- **标题**: format substring replace 函数边界行为
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `format` 按占位符拼接、`substring` 截取指定长度、`replace` 替换所有匹配子串。

## 做了什么
step 使用 `${{ format('Hello {0}', 'World') }}`、`${{ substring(atomgit.sha, 0, 7) }}`、`${{ replace(atomgit.ref, 'refs/heads/', '') }}` 并 echo 输出。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: FMT=Hello World | COVERED | `format('Hello {0}', 'World')` 求值后 echo 输出 |
| 2 | run_logs | positive | must_contain: SUB= | COVERED | `substring(atomgit.sha, 0, 7)` 截取前 7 位后 echo 输出 |
| 3 | run_logs | positive | must_contain: REP= | COVERED | `replace(atomgit.ref, 'refs/heads/', '')` 剥离前缀后 echo 输出 |
