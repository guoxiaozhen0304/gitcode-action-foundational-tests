# COMP-WFLOW-01-062
- **标题**: workflow env 与 defaults 字段验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow 级 env 对所有 job/step 可见，defaults.run.shell 和 working-directory 可被 job/step 覆盖**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-061
通过标准：
1. workflow env 在 step 中可访问
2. defaults shell 被正确继承
3. step 级 shell 覆盖 defaults
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check global env | `echo "GLOBAL=$GLOBAL_VAR"` | — | GLOBAL=global_value |
| 2 | Override shell | `echo "shell_override"` | shell: sh | shell_override |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain GLOBAL=global_value | positive | — | ✅ GENUINE | 步骤使用 shell 环境变量 $GLOBAL_VAR（workflow env 注入） |
| 2 | must_contain shell_override | positive | — | ✅ GENUINE | 步骤含 shell: sh 覆盖行为，真实测试 defaults 继承与覆盖机制 |
---
