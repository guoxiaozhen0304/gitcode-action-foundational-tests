# SEC-ARTF-01-001
- **标题**: fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原两条 artifact_download 断言为 MISSING_SOURCE（workflow 无下载步骤）。补上传完成标记步骤（test -f 真实校验后输出 FORK_ARTIFACT_UPLOADED，确定性锚点）；跨边界下载检查明确归属 harness（主仓上下文 API 检查，YAML 已注释）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain FORK_ARTIFACT_UPLOADED | ✅ GENUINE | 真实上传+校验后输出 |
| 2 | artifact_download | negative | must_not_equal success | ✅ COVERED | harness 主仓上下文跨边界下载检查 |
| 3 | artifact_download | positive | equals 404_or_permission_denied | ✅ COVERED | 同上 |
