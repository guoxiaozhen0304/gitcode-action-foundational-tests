# COMP-SCRIPT-01-081
- **标题**: 仓库内脚本执行与路径验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
断言原仅检查 inline echo（TRIVIAL），且缺 checkout（repo 脚本根本不存在，必走 fallback）。补 checkout；repo 脚本步骤改为存在性检查 + 真实执行（缺失则 exit 1）；断言指向 REPO_SCRIPT_RAN_OK。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain REPO_SCRIPT_RAN_OK | ✅ GENUINE | 真实执行仓库脚本后输出 |
| 2 | run_logs | negative | must_not_contain REPO_SCRIPT_MISSING | ✅ GENUINE | 脚本缺失时输出并 exit 1 |
