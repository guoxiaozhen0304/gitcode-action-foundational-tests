# COMP-TRIG-01-073

- **标题**: pull_request 事件关键字段与 types 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 pull_request 事件 PR number、title、state 等字段可访问，types 过滤生效。

## 做了什么
Steps: `echo "PR_NUM=${{ atomgit.event.pull_request.number }}"` 等 `${{ }}` 表达式；case 语句判断事件 action 是否在 types 白名单中。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain PR_NUM= | COVERED | `${{ }}` 上下文表达式（Rule 6） |
| 2 | run_logs | positive | must_contain pr_ok | COVERED | marker signal |
| 3 | run_logs | positive | must_contain type_in_filter | COVERED | case 语句真实判断 action ∈ {open,update,reopen} |
| 4 | run_logs | negative | must_not_contain type_out_of_filter | COVERED | type=negative 断言，case 语句 intentional 覆盖 |
