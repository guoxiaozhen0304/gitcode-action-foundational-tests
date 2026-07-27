# COMPAT-DIR-01-002
- **标题**: 工作流目录差异——.github/workflows/ 不应被识别
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**.github/workflows/ 下的工作流文件不被 GitCode 平台识别**
- 触发事件: `push`
- 规格引用: INTENT-COMPAT-029
通过标准：
1. .github/workflows/ 下的工作流不应被触发执行
2. 平台仅识别 .gitcode/workflows/ 目录
3. 不应出现来自 .github 目录的意外运行记录
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo if reached | `echo "GITHUB_DIR_WORKFLOW_RAN"` | — | GITHUB_DIR_WORKFLOW_RAN（不应出现） |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | with-github-dir |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_discovery 不应识别 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs 不应出现标记 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_status 仅 .gitcode 触发 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
