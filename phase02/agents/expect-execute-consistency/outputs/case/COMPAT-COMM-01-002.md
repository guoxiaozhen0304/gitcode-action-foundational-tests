# COMPAT-COMM-01-002
- **标题**: issue_comment types:created 不支持时应给出降级指引
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**若 types:created 不被支持，系统应明确报错或给出替代 types 列表**
- 触发事件: `issue_comment`
- 规格引用: INTENT-COMPAT-NEW-004
通过标准：
1. 不通过静默忽略
2. 报错信息包含可接受的 types 列表
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
| 1 | run_status 不应静默忽略 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 应含可接受 types | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
