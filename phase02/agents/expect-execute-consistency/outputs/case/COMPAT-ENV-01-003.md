# COMPAT-ENV-01-003
- **标题**: GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GITHUB_ENV 不应存在或被设置为空/未定义，不应被静默映射为 ATOMGIT_ENV 的值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-017
通过标准：
1. GITHUB_ENV 不等于 ATOMGIT_ENV
2. GITHUB_ENV 为空或未定义
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare env vars | `echo "GITHUB_ENV=$GITHUB_ENV" && echo "ATOMGIT_ENV=$ATOMGIT_ENV"` | — | GITHUB_ENV=, ATOMGIT_ENV=<文件路径> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs GITHUB_ENV != ATOMGIT_ENV | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs GITHUB_ENV 为空 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
