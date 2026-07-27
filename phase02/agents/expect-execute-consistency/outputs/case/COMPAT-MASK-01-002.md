# COMPAT-MASK-01-002
- **标题**: 通过 env 注入 secret 后输出应在日志中被脱敏
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**通过 env 注入 secret 后输出应在日志中被脱敏**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-033
通过标准：
1. 即使通过 env 间接引用，脱敏机制仍应生效
2. 不应出现明文的 secret 值
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | echo secret via env | env: MY_VAR=${{ secrets.TEST_SECRET }}; run: `echo "Env value: $MY_VAR"` | — | Env value: <secret值或***> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | TEST_SECRET |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_not_contain_secret TEST_SECRET | negative | deterministic | ✅ GENUINE | 步骤通过 env 块注入 ${{ secrets.TEST_SECRET }}，真实使用 secret，若 env 注入绕过脱敏则明文泄漏 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | *** 脱敏确认由 LLM 判定 |
| 3 | run_status equals success (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | run_status 由 LLM 判定 |
### 问题
- 断言2、3（LLM判定）被跳过；断言1 为 GENUINE
---
