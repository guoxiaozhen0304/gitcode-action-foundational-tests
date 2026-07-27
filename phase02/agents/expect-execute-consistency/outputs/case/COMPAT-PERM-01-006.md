# COMPAT-PERM-01-006
- **标题**: job 级 permissions 字段的支持度与降级方式
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**job 级 permissions 字段的支持度与降级方式**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-053
通过标准：
1. 含 job 级 permissions 的 workflow 不应被静默接受
2. 不支持时解析期明确报错
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark if job ran | `echo "JOB_LEVEL_PERM_JOB_RAN"` | — | JOB_LEVEL_PERM_JOB_RAN |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 静默接受行为由 LLM 判定 |
| 2 | save_result eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 解析期报错由 LLM 判定 |
| 3 | save_result eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 覆盖语义文档化由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
