# COMPAT-PERM-01-002
- **标题**: 未声明 permissions 时 fork PR 写操作隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**未声明 permissions 时 fork PR 写操作隔离**
- 触发事件: `fork_pr`
- 规格引用: INTENT-COMPAT-002
通过标准：
1. 系统对 fork PR 的默认 TOKEN 进行写操作隔离
2. 写操作被拒绝或失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | attempt write | git config + echo test + git add/commit/push | — | push 结果（成功或失败） |
## 3. 触发与运行环境
| 触发事件 | fork_pr |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | negative | — | ✅ GENUINE | fork PR 场景下 git push 应被拒绝，若写隔离失效 push 成功则 run_status 可为 success |
| 2 | run_logs must_not_contain_secret "" | negative | deterministic | ❌ UNEXERCISED | must_not_contain_secret 值为空字符串，无实际 secret 被引用，无法验证脱敏 |
### 问题
- 断言2 目标值为空字符串 "" 无意义（UNEXERCISED），step 中无 secrets 引用
---
