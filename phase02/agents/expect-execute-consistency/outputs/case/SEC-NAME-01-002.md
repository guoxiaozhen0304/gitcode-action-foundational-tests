# SEC-NAME-01-002
- **标题**: 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**printenv 和 /proc/self/environ 输出中 secret 值被脱敏**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-025
通过标准：
1. 日志不含 API_KEY 明文
2. 输出显示 masked_or_not_found
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Run printenv | `printenv \| grep API_KEY \|\| echo not found` | — | API_KEY 环境变量或 "not found" |
| 2 | Read proc environ | `cat /proc/self/environ \| tr '\0' '\n' \| grep API_KEY \|\| echo not found` | — | 同上 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | API_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 API_KEY 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | 步骤使用 printenv / /proc/self/environ 可能输出 secret 环境变量值；平台脱敏机制必须覆盖 |
| 2 | masked_or_not_found | positive | run_logs equals | ❌ VACUOUS | 步骤输出 "not found" 或 secret 值；不输出 "masked_or_not_found" 字面量 |
### 问题
断言 2 VACUOUS：步骤实际输出是 grep 结果或 "not found"，而非语义标签。
---
