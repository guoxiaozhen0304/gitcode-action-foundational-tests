# USE-CTX-01-001
- **标题**: 使用 atomgit 上下文时表达式正常求值
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`${{ atomgit.ref }}` 表达式正确求值为当前分支引用。

## 做了什么
step `echo "ref=${{ atomgit.ref }}"` 显式输出 ref 值。断言检查日志中是否包含 `ref=refs/heads/`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"ref=refs/heads/" | COVERED | step 通过 `${{ atomgit.ref }}` 显式 echo ref 值，精确匹配前缀模式 |
