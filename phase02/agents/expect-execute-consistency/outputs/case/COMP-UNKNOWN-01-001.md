# COMP-UNKNOWN-01-001
- **标题**: 包含未知顶层字段的 workflow 触发 YAML 校验失败
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**包含未知顶层字段的 workflow 触发 YAML 校验失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-002
通过标准：
1. workflow 提交后触发校验失败（正向）
2. 错误信息包含字段名及不支持语义（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo step | `echo "should not run"` | - | should not run |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: validation_failed | ✅ COVERED | YAML 含 `unknown_field: true` 语法错误，断言期望 run_status != COMPLETED，平台校验应拒绝该 YAML |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估错误信息是否包含不支持的字段名及行号 |
---
