# COMP-RUNNER-01-003
- **标题**: 不存在的标签组合导致 job 排队或失败
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**不存在的标签组合导致 job 排队或失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-010
通过标准：
1. job 不应成功执行（负向）
2. 系统应给出标签无匹配的提示（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo | `echo "should not run"` | - | should not run |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | ✅ GENUINE | runs-on: [nonexistent-os, x64, small] 的标签组合不存在，平台调度器应拒绝或超时，run 不应成功 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估错误信息是否包含标签匹配提示 |
---
