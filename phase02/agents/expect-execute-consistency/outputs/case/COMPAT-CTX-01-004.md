# COMPAT-CTX-01-004
- **标题**: atomgit.actor 规格自相矛盾的实测仲裁
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**atomgit.actor 有确定行为：返回触发者用户名，或被明确定义为不支持**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-040
通过标准：
1. atomgit.actor 求值得到确定结果
2. 不应维持规格自相矛盾而不作任何记录
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo atomgit actor value | `echo "ACTOR_VALUE=${{ atomgit.actor }}" && echo "PROBE_DONE"` | — | ACTOR_VALUE=<触发者用户名>, PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain PROBE_DONE | positive | — | ✅ GENUINE | 步骤使用 `${{ atomgit.actor }}` 表达式，真实验证平台上下文 |
| 2 | run_logs ACTOR_VALUE 触发者用户名 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs 三方不一致检测 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
