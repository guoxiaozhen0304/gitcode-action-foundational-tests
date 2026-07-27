# SEC-COMM-01-002
- **标题**: 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**精确指令评论正常触发，但引用块/反讽/代码块内嵌指令不触发**
- 触发事件: `pull_request_comment` (as untrusted_contributor)
- 规格引用: INTENT-SEC-042
通过标准：
1. 精确指令触发
2. 边界评论不触发
3. 触发可回溯
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark trigger | `echo "TRIGGERED_BY_COMMENT: command accepted"` | — | 触发标记 |

## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 精确指令触发 | positive | run_trigger equals "exact_command_triggers" | ❌ MISSING_SOURCE | target=run_trigger 非 run_logs/run_status，步骤不产生此输出 |
| 2 | 边界评论不触发 | negative | run_trigger must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 3 | 触发可回溯 | nonfunctional | trigger_audit equals | 🔶 LLM_DEPENDENT | nonfunctional + external target |
### 问题
所有断言 target=run_trigger / trigger_audit，均为非标准外部目标，workflow 步骤仅 echo 标记字符串，无法驱动这些断言验证。
---
