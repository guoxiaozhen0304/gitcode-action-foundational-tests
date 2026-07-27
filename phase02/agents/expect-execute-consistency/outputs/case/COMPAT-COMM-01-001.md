# COMPAT-COMM-01-001
- **标题**: issue_comment types 命名差异 - GitCode 合法 types 应被接受
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GitCode 合法 types（created/edited/deleted）应被接受并正常触发**
- 触发事件: `issue_comment`
- 规格引用: INTENT-COMPAT-NEW-004
通过标准：
1. GitCode 风格 types 命名被接受
2. 不因命名差异导致误报错误
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo trigger info | `echo "event_name=${{ atomgit.event_name }}"` | — | event_name=issue_comment |
## 3. 触发与运行环境
| 触发事件 | issue_comment |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | validation_error 不应被拒绝 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
