# COMPAT-DIR-01-003
- **标题**: .github/workflows 目录不应被识别且应给出迁移提示
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**.github/workflows 下的 workflow 不应被识别，系统应给出迁移提示**
- 触发事件: `push`
- 规格引用: INTENT-COMPAT-029
通过标准：
1. .github/workflows 下的 workflow 不应被触发
2. 系统给出迁移提示，说明正确的目录位置
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | — | hello（若被识别则出现） |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status 不应被触发 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 迁移提示 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
