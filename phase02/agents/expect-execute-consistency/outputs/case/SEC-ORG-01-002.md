# SEC-ORG-01-002
- **标题**: fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**fork PR 下组织级 secret 与项目级同等隔离，日志命中数为 0**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-039
通过标准：
1. 日志不含 ORG_SHARED_KEY 原值
2. fork PR 下 secret 被隔离
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt to echo org secret | `echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"` | — | secret 值或空 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | org-scoped-secret |
| Secrets | ORG_SHARED_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 ORG_SHARED_KEY 原值 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.ORG_SHARED_KEY }} → NEVER VACUOUS；fork PR 隔离 |
| 2 | fork PR 组织级 secret 被隔离 | positive | run_logs equals "fork_pr_org_secret_isolated" | ❌ VACUOUS | echo 输出 "ORG_SECRET_VALUE: ..."，不输出语义标签 |
### 问题
断言 2 VACUOUS：步骤不输出标签字符串。
---
