# SEC-MASK-01-005
- **标题**: Secret 日志脱敏不可通过多行值输出绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**多行 secret 的每一行在日志中均被脱敏，换行符不成为脱敏边界**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-007
通过标准：
1. 日志不含 MULTI_LINE_SECRET 明文
2. 多行均显示为 ***
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo multiline secret | `echo "${{ secrets.MULTI_LINE_SECRET }}"` | — | 多行 secret 值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | MULTI_LINE_SECRET |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 secret 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.MULTI_LINE_SECRET }} → NEVER VACUOUS |
| 2 | 多行脱敏为 *** | positive | run_logs equals "multiline_masked_with_asterisks" | ❌ VACUOUS | echo 输出的是 *** 文本，不输出语义标签字符串 |
### 问题
断言 2 VACUOUS：步骤输出 ***，断言期望的是 "multiline_masked_with_asterisks" 标签字符串。
---
