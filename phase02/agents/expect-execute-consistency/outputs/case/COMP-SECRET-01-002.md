# COMP-SECRET-01-002
- **标题**: secret 原始值不应以明文出现在标准日志中
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**secret 原始值不应以明文出现在标准日志中**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-012
通过标准：
1. 日志中不包含 secret 原始明文（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo secret via env | `env: MY_SECRET=${{ secrets.TEST_SECRET }}` → `echo "env secret is $MY_SECRET"` | - | env secret is *** |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [TEST_SECRET] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: TEST_SECRET | ✅ GENUINE | 步骤通过 env 注入 `${{ secrets.TEST_SECRET }}` 并 echo，平台脱敏后不应出现明文 secret |
---
