# COMP-TRIG-01-077

- **标题**: pull_request_comment 事件关键字段与过滤验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 pull_request_comment 事件 PR number、comment.body 字段可访问。

## 做了什么
Steps: `echo "PR_NUM=${{ atomgit.event.pull_request.number }}"`、`echo "COMMENT_BODY=${{ atomgit.event.comment.body }}"`——`${{ }}` 表达式。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain PR_NUM= | COVERED | `${{ atomgit.event.pull_request.number }}` 上下文表达式（Rule 6） |
| 2 | run_logs | positive | must_contain pr_comment_ok | COVERED | marker signal |
