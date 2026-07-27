# COMP-UNKNOWN-01-002
- **标题**: 不应静默忽略未知字段导致用户误以为配置生效
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**不应静默忽略未知字段导致用户误以为配置生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-002
通过标准：
1. 运行不应在未知字段被静默忽略的情况下成功完成（负向）
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
| 1 | run_status | negative | equals: success_with_unknown_field_silently_ignored | ✅ GENUINE | harness 注入未知字段后 dispatch，验证平台不应静默忽略未知字段而让 run 成功 |
---
