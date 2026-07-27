# COMPAT-PATHS-01-002
- **标题**: paths 过滤器 301 条越界测试
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**paths 过滤器 301 条越界测试**
- 触发事件: `push` (triggered on branch main)
- 规格引用: INTENT-COMPAT-012
通过标准：
1. 平台应对超出 300 条上限的 paths 给出明确的校验错误
2. 超出上限的 paths 不应被静默接受
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo paths ok | `echo "PATHS_301_OK"` | — | PATHS_301_OK |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | negative | — | ✅ GENUINE | 301 条 paths 若被正确拒绝，run_status 不会是 success；断言反映平台校验能力 |
| 2 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 错误信息质量由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过；断言1 为 GENUINE
---
