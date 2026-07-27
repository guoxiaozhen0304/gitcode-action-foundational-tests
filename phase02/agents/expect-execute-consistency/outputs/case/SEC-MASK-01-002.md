# SEC-MASK-01-002
- **标题**: Secret 值在 step summary 和错误堆栈中必须被脱敏
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**step summary 和错误堆栈中 secret 原值被 *** 替代**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-004
通过标准：
1. step_summary 不含 API_KEY 原值
2. error_stack 不含 API_KEY 原值
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write secret to summary | `echo "Key: ${{ secrets.API_KEY }}" >> $ATOMGIT_STEP_SUMMARY` | — | summary 内容 |
| 2 | Intentionally fail | `echo "Failing with key ${{ secrets.API_KEY }}"`; `exit 1` | — | 错误日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | API_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary 不含 secret | negative | must_not_contain_secret | ❌ UNEXERCISED | target=step_summary 非 run_logs；步骤写入 summary，但断言针对的是 step_summary 独立目标 |
| 2 | error_stack 不含 secret | negative | must_not_contain_secret | ❌ UNEXERCISED | target=error_stack 非 run_logs；步骤有 exit 1 产生堆栈，但断言目标非标准 |
### 问题
两个断言 target 均为非标准外部目标（step_summary / error_stack），虽步骤有 secret 使用和 exit 1，但断言格式要求对应目标存在源步骤。
---
