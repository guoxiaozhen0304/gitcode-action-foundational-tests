# SEC-COMM-01-001
- **标题**: issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**伪装在代码块中的关键字不应触发 workflow**
- 触发事件: `issue_comment` (as untrusted_contributor)
- 规格引用: INTENT-SEC-026
通过标准：
1. 伪装关键字不应触发运行
2. workflow 不应被触发
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check trigger | `echo "Triggered by comment"` | — | "Triggered by comment" |

## 3. 触发与运行环境
| 触发事件 | issue_comment |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不触发 | negative | run_status must_not_equal "triggered_by_masked_keyword" | ⚠️ STATUS_GUARANTEED | 步骤仅 echo，一旦触发必然成功；断言值 "triggered_by_masked_keyword" 为外部映射概念，不存在于步骤输出中 |
| 2 | workflow_not_triggered | positive | run_logs equals "workflow_not_triggered" | ❌ VACUOUS | 步骤从未输出 "workflow_not_triggered"；若 workflow 被触发执行，输出为 "Triggered by comment"；该断言字符串仅存在于期望中 |
### 问题
断言 1 STATUS_GUARANTEED 且断言 2 VACUOUS：两者均依赖外部判定器将触发与否映射为字符串，步骤本身无法区分触发绕过结果。
---
