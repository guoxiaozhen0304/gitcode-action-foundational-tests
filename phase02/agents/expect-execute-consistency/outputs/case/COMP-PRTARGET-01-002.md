# COMP-PRTARGET-01-002
- **标题**: 显式 checkout head.sha 后执行不可信代码的风险可控
- **维度**: 完备性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**显式 checkout head.sha 后执行不可信代码的风险可控**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-014
通过标准：
1. checkout head.sha 成功（正向）
2. workflow 文件仍为 base 分支版本（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout head sha | `uses: checkout` with `ref: ${{ atomgit.event.pull_request.head.sha }}` | - | runner/action 日志 |
| 2 | Verify workflow still base | `echo "BASE_VERSION_MARKER"` | - | BASE_VERSION_MARKER |
## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | 步骤使用 uses: checkout + `${{ }}` 表达式，有实质平台行为 |
| 2 | run_logs | positive | contains: BASE_VERSION_MARKER | ❌ VACUOUS | 步骤仅 echo 字面量，未验证 base 分支版本语义 |
### 问题
**断言 2 — VACUOUS**: 步骤仅 echo 了字面量 BASE_VERSION_MARKER，未验证 workflow 文件确实来自 base 分支（而非 fork 分支）。虽然有 checkout head.sha，但该 marker 并不能证明 workflow 文件版本来源。
---
