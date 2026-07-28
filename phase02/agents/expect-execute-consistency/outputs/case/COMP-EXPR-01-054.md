# COMP-EXPR-01-054
- **标题**: 字符串函数 contains startsWith endsWith 边界行为
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
contains 子串匹配、startsWith 前缀匹配、endsWith 后缀匹配正确，区分大小写。

## 做了什么
1. step `Contains match`（if: ${{ contains(atomgit.ref_name, 'main') }}）：`echo "contains_passed"`
2. step `StartsWith match`（if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}）：`echo "startswith_passed"`
3. step `EndsWith match`（if: ${{ endsWith(atomgit.ref_name, 'ain') }}）：`echo "endswith_passed"`
4. step `Case mismatch check`：`echo "CASE_MATCH=${{ contains('main', 'MAIN') }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: contains_passed | COVERED | if 条件成立时 step 执行并 echo |
| 2 | run_logs | positive | must_contain: startswith_passed | COVERED | if 条件成立时 step 执行并 echo |
| 3 | run_logs | positive | must_contain: endswith_passed | COVERED | if 条件成立时 step 执行并 echo |
| 4 | run_logs | positive | must_contain: CASE_MATCH=false | COVERED | ${{ contains('main', 'MAIN') }} 表达式求值为 false |
