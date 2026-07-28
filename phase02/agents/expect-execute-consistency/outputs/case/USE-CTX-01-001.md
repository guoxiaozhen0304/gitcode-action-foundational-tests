# USE-CTX-01-001
- **标题**: 使用 atomgit 上下文时表达式正常求值
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
`${{ atomgit.ref }}` 表达式正确求值为当前分支引用。

## 做了什么
workflow step 中 `echo "ref=${{ atomgit.ref }}"` 引用 atomgit 上下文。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: ref=refs/heads/ | COVERED | `echo "ref=${{ atomgit.ref }}"` — `${{ }}` 真实表达式，输出匹配 refs/heads/ 前缀 |

