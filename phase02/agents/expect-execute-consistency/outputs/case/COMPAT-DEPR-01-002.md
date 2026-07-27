# COMPAT-DEPR-01-002
- **标题**: ::add-path:: 废弃命令应被拒绝或给出迁移指引
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统应明确拒绝 ::add-path:: 命令或给出弃用警告及替代方案**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-012
通过标准：
1. 不通过命令被静默忽略且 workflow 成功
2. 系统给出明确响应
3. 若给出警告应包含 ATOMGIT_PATH 替代示例
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use deprecated add-path | `echo '::add-path::/custom/path' && echo "PATH=$PATH"` | — | PATH=..., done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status 不静默忽略 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 明确响应 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | error_message ATOMGIT_PATH 替代 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
