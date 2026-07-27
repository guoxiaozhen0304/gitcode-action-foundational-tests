# COMPAT-CTX-01-001
- **标题**: 使用 github.ref 上下文应报错或求值为空
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**平台应对 github.* 上下文给出明确报错，或在运行时求值为空字符串**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-016
通过标准：
1. 使用 github.ref 不应被静默映射为 atomgit.ref
2. 报错信息应提示将 github.* 替换为 atomgit.*
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo github ref | `echo "github_ref=${{ github.ref }}"` | — | github_ref=（空或报错） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs github_ref 为空或失败 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 提示替换 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
