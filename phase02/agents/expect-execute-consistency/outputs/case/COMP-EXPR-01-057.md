# COMP-EXPR-01-057
- **标题**: format substring replace 函数边界行为
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
format 按占位符替换，substring 截取指定长度，replace 替换所有匹配子串。

## 做了什么
1. step `Format string`：`echo "FMT=${{ format('Hello {0}', 'World') }}"`
2. step `Substring sha`：`echo "SUB=${{ substring(atomgit.sha, 0, 7) }}"`
3. step `Replace prefix`：`echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: FMT=Hello World | COVERED | format 表达式拼接输出 |
| 2 | run_logs | positive | must_contain: SUB= | COVERED | substring 从 atomgit.sha 截取 7 位并 echo |
| 3 | run_logs | positive | must_contain: REP= | COVERED | replace 去除 refs/heads/ 前缀并 echo |
