# COMP-UNKNOWN-01-005
- **标题**: 顶层 inputs 与 manual_override 字段的实际处理记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**顶层 inputs 的 default 注入与 manual_override 对手动触发表单的实际影响**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-031
通过标准：
1. 顶层 inputs 的 default 是否注入 inputs 上下文
2. manual_override 对手动触发表单/参数覆盖的实际影响
3. 不应出现参数声明无效的静默忽略
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo top input | `echo "TOP_INPUT=${{ inputs.branch_name }}"` | — | TOP_INPUT=main |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain TOP_INPUT= | positive | — | ✅ GENUINE | 步骤使用 `${{ inputs.branch_name }}` 表达式，真实验证平台 inputs 注入行为 |
| 2 | top_inputs_handling | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 逐字记录 inputs 处理 |
| 3 | silent_ignore | negative | llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 判断静默忽略 |
### 问题
(无)
---
