# COMP-TRIG-01-080
- **标题**: 触发事件别名 pr_comment 的有效性与等价性记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**触发事件别名 pr_comment 的有效性与等价性记录**
- 触发事件: `pull_request_comment`
- 规格引用: INTENT-COMP-024
通过标准：
1. on.pr_comment 的实际处理逐字记录（正向/记录）
2. pull_request_comment 的 comments 正则过滤行为回归保护（正向）
3. 非法事件名不应静默保存导致永不触发（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark comment trigger | `echo "PR_COMMENT_TRIGGERED"` | - | PR_COMMENT_TRIGGERED |
## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | maintainer |
| Repo 环境 | pr-comment-alias |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | alias_handling | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估 on.pr_comment 的平台处理行为 |
| 2 | silent_ignore | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估是否出现静默忽略 |
---
