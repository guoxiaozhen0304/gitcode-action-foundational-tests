# COMPAT-CTX-01-002
- **标题**: 使用 atomgit.ref 上下文应正确返回触发引用
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**atomgit.ref 应正确返回触发事件的引用（如 refs/heads/main）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-016
通过标准：
1. 日志中 atomgit_ref 的值不为空且符合预期格式
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo atomgit ref | `echo "atomgit_ref=${{ atomgit.ref }}"` | — | atomgit_ref=refs/heads/main |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | — | ✅ GENUINE | 步骤使用 `${{ atomgit.ref }}` 表达式，真实验证平台上下文注入 |
| 2 | run_logs atomgit_ref 非空引用值 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
