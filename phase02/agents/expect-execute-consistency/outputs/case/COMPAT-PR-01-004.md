# COMPAT-PR-01-004
- **标题**: PR types 含 merge 时不触发与 GitHub 行为差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 GitCode 对 `pull_request.types: [open, merge]` 的触发行为——merge 事件是否会产生独立的 pull_request merge 运行而非仅 PUSH 运行。

## 做了什么
workflow 在 `pull_request.types: [open, merge]` 触发时执行 `echo "event_name=${{ atomgit.event_name }}"` 和 `echo "done"`。上下文变量输出提供触发事件证据。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | "合并PR后不应仅产生PUSH运行" | COVERED | step输出${{ atomgit.event_name }}为GENUINE(R1)，日志可观测事件类型以判断是否仅PUSH |
| 2 | run_status | positive | "若平台已修复合并后应触发pull_request运行" | COVERED | run_status为平台日志可观测(GENUINE) |
