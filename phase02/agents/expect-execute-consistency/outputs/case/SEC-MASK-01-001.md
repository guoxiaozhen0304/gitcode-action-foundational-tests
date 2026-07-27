# SEC-MASK-01-001
- **标题**: Secret 值在运行日志中必须被自动脱敏为 ***
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**echo secret 后日志中 secret 原值被 *** 替代，全文命中数为 0**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-004
通过标准：
1. 日志不含 DEPLOY_TOKEN 明文
2. 脱敏标记 *** 出现
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo secret directly | `echo "The secret is ${{ secrets.DEPLOY_TOKEN }}"` | — | 脱敏后的 secret |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 DEPLOY_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.DEPLOY_TOKEN }} → NEVER VACUOUS；脱敏由平台机制执行 |
| 2 | 脱敏为 *** | positive | run_logs equals "masked_with_asterisks" | ❌ VACUOUS | echo 输出的是脱敏后的文本（***），步骤不输出 "masked_with_asterisks" 字面量；该值为外部映射 |
### 问题
断言 2 VACUOUS：步骤输出 ***，而非语义标签字符串 "masked_with_asterisks"。
---
