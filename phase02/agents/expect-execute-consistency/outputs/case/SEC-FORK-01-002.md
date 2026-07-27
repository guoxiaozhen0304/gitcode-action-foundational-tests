# SEC-FORK-01-002
- **标题**: fork PR 中 secrets 引用返回空值且 job 不崩溃
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**fork PR 下 secrets.API_KEY 返回空，环境变量未设置，job 成功完成**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-001
通过标准：
1. 日志不含 API_KEY 明文
2. run_status 为 success
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check env empty | `if [ -z "$API_KEY" ]; then echo "API_KEY is empty..."; else echo "API_KEY is not empty"; exit 1; fi` | env: API_KEY=${{ secrets.API_KEY }} | 空值检测 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-secrets |
| Secrets | API_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 API_KEY 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | env 中使用 ${{ secrets.API_KEY }} → NEVER VACUOUS；fork PR 隔离机制 |
| 2 | run_status success | positive | run_status equals "success" | ✅ GENUINE | 步骤有 if/exit 1 分支；fork PR 下 secret 为空 → 打印 "API_KEY is empty" → success |
### 问题
(无)
---
