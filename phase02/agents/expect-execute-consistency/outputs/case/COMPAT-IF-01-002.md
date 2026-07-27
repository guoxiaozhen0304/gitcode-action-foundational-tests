# COMPAT-IF-01-002
- **标题**: continue-on-error 标记后失败 step 不阻断后续执行
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**continue-on-error 标记后失败 step 不阻断后续执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-003
通过标准：
1. 第一个 step 虽失败，但因 continue-on-error 标记，后续 step 仍继续执行
2. job 未在第一个 step 处中断
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | force failure with continue | `exit 1`（continue-on-error: true） | — | 非零退出码 + (failed) 标记 |
| 2 | should still run | `echo "This should appear"` | — | "This should appear" |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "This should appear" | positive | — | ✅ GENUINE | continue-on-error: true 允许后续 step 执行，echo 输出需真实运行才能出现 |
| 2 | run_status equals success | positive | — | ✅ GENUINE | 因 continue-on-error: true，失败不中断 job，最终状态可能为 success |
---
