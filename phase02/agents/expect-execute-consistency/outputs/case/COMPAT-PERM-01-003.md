# COMPAT-PERM-01-003
- **标题**: permissions 命名差异——GitHub contents 权限项应报错
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**permissions 命名差异——GitHub contents 权限项应报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-030
通过标准：
1. 使用 `contents` 时 workflow 解析/校验阶段应报错
2. 不应静默忽略导致实际权限与预期不符
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | attempt clone | uses: checkout | — | — |
| 2 | should not reach | `echo "CONTENTS_PERM_ACCEPTED"` | — | CONTENTS_PERM_ACCEPTED（若静默接受） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_parse eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 解析阶段行为由 LLM 判定 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 错误信息由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | CONTENTS_PERM_ACCEPTED 由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
