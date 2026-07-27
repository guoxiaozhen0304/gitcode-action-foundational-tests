# COMP-RUNNER-01-081
- **标题**: 四段式 runs-on（codearts-hosted 首段）调度行为裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**四段式 runs-on（codearts-hosted 首段）调度行为裁定**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-029
通过标准：
1. 四段式的调度结果与首段语义逐字记录（正向/记录）
2. 三段式调度行为回归（正向）
3. 任一形式被接受后不应调度到与标签声明不符的 Runner（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print runner identity | `${{ runner.name }}`, `${{ runner.os }}` | - | 平台上下文变量值 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: RUNNER_NAME= | ✅ GENUINE | `${{ runner.name }}` 为平台上下文表达式，输出 Runner 真实身份 |
| 2 | runner_identity | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估 codearts-hosted 首段语义与调度结果一致性 |
| 3 | runner_mismatch | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估是否出现标签不匹配且无提示 |
---
