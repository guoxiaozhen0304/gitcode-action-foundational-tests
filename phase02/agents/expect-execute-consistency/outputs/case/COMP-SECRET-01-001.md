# COMP-SECRET-01-001
- **标题**: echo secret 在日志中被脱敏为 ***
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**echo secret 在日志中被脱敏为 *****
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-012
通过标准：
1. 日志中包含 *** 而非真实 secret 值（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo secret | `echo "secret is ${{ secrets.TEST_SECRET }}"` | - | 平台脱敏后的日志 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [TEST_SECRET] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: *** | ✅ GENUINE | 步骤通过 `${{ secrets.TEST_SECRET }}` 输出 secret 值，platform 脱敏机制产生 `***`，真实测试了 secret 遮蔽行为 |
| 2 | run_logs | negative | must_not_contain_secret: TEST_SECRET | ✅ GENUINE | 步骤使用了 TEST_SECRET，断言验证平台不会在日志中暴露明文 |
---
