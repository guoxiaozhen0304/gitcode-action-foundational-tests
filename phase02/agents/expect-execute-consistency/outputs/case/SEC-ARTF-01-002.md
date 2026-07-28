# SEC-ARTF-01-002
- **标题**: 跨仓库 artifact 下载返回 403 或 404
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
curl 命令原含字面 `\n` 断行错误已修复；步骤改为真实判定 HTTP 状态码：403/404 输出 CROSS_REPO_BLOCKED_OK，200 输出 CROSS_REPO_DOWNLOAD_LEAKED 并 exit 1；断言 2 原 VACUOUS（期望字面值 403_or_404 无源）已替换为标记断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain CROSS_REPO_BLOCKED_OK | ✅ GENUINE | 真实 curl + 状态码判断输出 |
| 2 | run_logs | negative | must_not_contain CROSS_REPO_DOWNLOAD_LEAKED | ✅ GENUINE | 200 时输出并 exit 1 |
