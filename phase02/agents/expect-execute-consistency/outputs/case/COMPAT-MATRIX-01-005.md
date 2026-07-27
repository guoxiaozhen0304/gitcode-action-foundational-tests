# COMPAT-MATRIX-01-005
- **标题**: matrix exclude 全排除不被支持时的差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**matrix exclude 全排除不被支持时的差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-007
通过标准：
1. 系统对空矩阵给出明确报错
2. 不通过 exclude 被静默忽略导致所有实例仍生成
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo matrix values | echo os/node via ${{ matrix.os }}, ${{ matrix.node }} | — | os/node 值或报错 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 空矩阵报错由 LLM 判定 |
| 2 | run_status eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 静默忽略由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
