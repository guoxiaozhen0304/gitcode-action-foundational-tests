# COMPAT-MATRIX-01-003
- **标题**: matrix 三维展开不被支持时的差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**matrix 三维展开不被支持时的差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-007
通过标准：
1. 系统对三维 matrix 给出明确响应（接受或拒绝）
2. 不通过静默忽略导致 matrix 配置失效
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo matrix values | echo os/node/browser via ${{ matrix.os }} 等 | — | os/node/browser 值 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 三维 matrix 是否接受由 LLM 判定 |
| 2 | run_status eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 静默忽略行为由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
