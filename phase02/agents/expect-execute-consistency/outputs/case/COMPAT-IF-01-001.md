# COMPAT-IF-01-001
- **标题**: step 失败后后续 step 默认跳过行为
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**step 失败后后续 step 默认跳过行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-003
通过标准：
1. 第一个 step 失败后，第二个 step 被系统默认跳过
2. 整个 job 标记为失败状态
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | force failure | `exit 1` | — | 非零退出码，step 失败 |
| 2 | should be skipped | `echo "This should not appear"` | — | "This should not appear"（若未跳过） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals failure | positive | — | ✅ GENUINE | 步骤1 故意 exit 1 导致失败，步骤2 无 continue-on-error 或 always()，失败后应被跳过，run_status 应为 failure |
| 2 | run_logs contains "This should not appear" | negative | — | ✅ GENUINE | 验证跳过语义：若 skip 语义正确实现，"This should not appear" 不应出现 |
---
