# COMPAT-LIMIT-01-002
- **标题**: workflow_dispatch 输入数量上限与非默认分支可用性
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**workflow_dispatch 输入数量上限与非默认分支可用性**
- 触发事件: `workflow_dispatch` (on_branch: non-default-branch-probe)
- 规格引用: INTENT-COMPAT-052
通过标准：
1. 26 个 inputs 的保存期行为确定（报错或截断）
2. 非默认分支 dispatch 可用性结论确定
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark dispatch run | `echo "DISPATCH_LIMIT_PROBE_RAN"` | — | DISPATCH_LIMIT_PROBE_RAN |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch (on_branch: non-default-branch-probe) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 保存期响应由 LLM 判定 |
| 2 | save_result eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 静默接受行为由 LLM 判定 |
| 3 | run_list eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 非默认分支可用性由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
