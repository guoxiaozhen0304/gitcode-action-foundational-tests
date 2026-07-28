# SEC-ARTF-01-001
- **标题**: fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- **维度**: security
- **评级**: 断言一致

## 想测什么
fork PR 上传 artifact 后，主仓不应能下载该 artifact。

## 做了什么
fork PR workflow 真实上传 artifact 并输出 FORK_ARTIFACT_UPLOADED；harness 在主仓侧执行 artifact_download 跨边界检查。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "FORK_ARTIFACT_UPLOADED" | COVERED | 对应"fork 贡献者上传 artifact"；workflow echo→GENUINE |
| 2 | artifact_download | negative | must_not_equal "success" | COVERED | 对应"主仓不可下载 fork PR artifact"；harness 跨边界 API 检查→GENUINE |
| 3 | artifact_download | positive | equals "404_or_permission_denied" | COVERED | 对应"返回 404 或权限拒绝"；harness 判定 |
