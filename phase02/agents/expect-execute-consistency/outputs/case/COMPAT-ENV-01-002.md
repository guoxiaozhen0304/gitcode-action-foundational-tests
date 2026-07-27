# COMPAT-ENV-01-002
- **标题**: GITHUB_SHA 环境变量在 GitCode 中应为空或未定义
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**$GITHUB_SHA 应为空字符串或未定义，不应被错误映射到 ATOMGIT_SHA**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-017
通过标准：
1. GITHUB_SHA 不应被静默映射为 ATOMGIT_SHA
2. 运行日志中应能区分 GITHUB_SHA 为空
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo GITHUB_SHA | `echo "github_sha=$GITHUB_SHA"` | — | github_sha=（空或未定义） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs github_sha 为空 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 提示替换 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
