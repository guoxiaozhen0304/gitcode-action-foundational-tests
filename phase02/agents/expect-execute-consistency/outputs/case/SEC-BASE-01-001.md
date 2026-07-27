# SEC-BASE-01-001
- **标题**: pull_request_target 使用 base 分支的 workflow 版本
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**pull_request_target 触发时加载 base 分支 workflow，fork PR 的改动不被采用**
- 触发事件: `pull_request_target` (as maintainer)
- 规格引用: INTENT-SEC-035
通过标准：
1. base 分支 workflow 被执行
2. fork 注入步骤不出现在日志
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo from base | `echo "Executing base branch workflow"` | — | "Executing base branch workflow" |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | base 分支 workflow 被执行 | positive | run_logs equals "base_branch_workflow_executed" | ❌ VACUOUS | 步骤仅 echo 固定字符串 "Executing base branch workflow"，断言期望 "base_branch_workflow_executed"；该字面量从未被步骤输出，属于外部映射 |
| 2 | 不含 fork_injected_step | negative | run_logs must_not_contain "fork_injected_step" | ✅ GENUINE | 步骤确实不产生该字符串；依赖平台行为确保 fork PR 的注入步骤不会被执行 |
### 问题
断言 1 VACUOUS：步骤输出与断言期望的字符串不匹配，该字符串仅存在于断言逻辑中。
---
