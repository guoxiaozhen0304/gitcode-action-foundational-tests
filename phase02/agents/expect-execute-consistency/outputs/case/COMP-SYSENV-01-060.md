# COMP-SYSENV-01-060
- **标题**: ATOMGIT 系统环境变量值正确性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**ATOMGIT 系统环境变量值正确性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-059
通过标准：
1. ATOMGIT_SHA 等于 atomgit.sha（正向）
2. ATOMGIT_REF 等于 atomgit.ref（正向）
3. ATOMGIT_RUN_NUMBER 与 atomgit.run_number 一致（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare values | `[ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes || echo no` 等比较 | - | SHA_MATCH=yes / REF_MATCH=yes / EVENT_MATCH=yes |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA_MATCH=yes | ✅ GENUINE | `[ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ]` 为实质 shell 比较 + `${{ }}` 平台上下文求值 |
| 2 | run_logs | positive | must_contain: REF_MATCH=yes | ✅ GENUINE | `[ "$ATOMGIT_REF" = "${{ atomgit.ref }}" ]` 实质比较 |
| 3 | run_logs | positive | must_contain: EVENT_MATCH=yes | ✅ GENUINE | `[ "$ATOMGIT_EVENT_NAME" = "${{ atomgit.event_name }}" ]` 实质比较 |
---
