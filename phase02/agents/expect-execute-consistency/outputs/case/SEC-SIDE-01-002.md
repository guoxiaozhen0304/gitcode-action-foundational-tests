# SEC-SIDE-01-002
- **标题**: Secret 不经 artifact 侧信道绕过脱敏外泄
- **维度**: security
- **评级**: 部分不符

## 想测什么
Artifact 中不应包含 secret 明文；若包含应被拦截或遮蔽。

## 做了什么
step 将 `${{ secrets.DEPLOY_TOKEN }}` 写入文件后使用 upload-artifact 上传。无 step 下载 artifact 验证内容。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_content | negative | must_not_contain_secret:DEPLOY_TOKEN | MISSING_SOURCE | artifact 内容需外部下载后检查，workflow 内无任何 step 读取或验证 artifact 内容 |
| 2 | run_status | positive | equals:blocked_or_masked | COVERED | 平台行为（上传被拦截或遮蔽），通过 run_status 可观察 |
