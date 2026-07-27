# COMPAT-ISOLATE-01-002
- **标题**: Runner 环境隔离——跨 job 环境变量隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**Runner 环境隔离——跨 job 环境变量隔离**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-028
通过标准：
1. job B 中不应读取到 job A 通过 ATOMGIT_ENV 设置的值
2. $ATOMGIT_ENV 的作用域仅限于当前 job
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | job-set-env: set env in job A | echo to $ATOMGIT_ENV + echo ENV_SET_IN_JOB_A | — | ENV_SET_IN_JOB_A |
| 2 | job-verify-env: verify env not leaked | bash if 判断 ISOLATION_TEST_KEY → ENV_ISOLATED_OK/ENV_ISOLATION_BROKEN | — | 隔离结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | ENV_ISOLATED_OK 由 LLM 判定 |
| 2 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | ENV_ISOLATION_BROKEN 由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | ENV_SET_IN_JOB_A 由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
