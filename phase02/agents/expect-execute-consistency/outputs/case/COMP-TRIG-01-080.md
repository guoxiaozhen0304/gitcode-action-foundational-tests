# COMP-TRIG-01-080

- **标题**: 触发事件别名 pr_comment 的有效性与等价性记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
记录 on.pr_comment 别名的平台处理行为（与 pull_request_comment 等价性）。

## 做了什么
on: pr_comment，step: `echo "PR_COMMENT_TRIGGERED"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | alias_handling | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工逐字记录校验/触发行为 |
| 2 | silent_ignore | negative | eval=llm_assisted | LLM_DEPENDENT | 需人工判断是否静默忽略 |
