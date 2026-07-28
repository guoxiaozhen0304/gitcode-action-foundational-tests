# SEC-SIDE-01-002
- **标题**: Secret 不经 artifact 侧信道绕过脱敏外泄
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
Artifact 中不应包含 secret 明文。

## 做了什么
workflow 将 secret 写入文件并上传为 artifact，harness 下载检查内容。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_content | negative | must_not_contain_secret: DEPLOY_TOKEN | COVERED | `echo "token=${{ secrets.DEPLOY_TOKEN }}" > secret.txt` 并 upload-artifact，harness 下载检查明文 |
| 2 | run_status | positive | blocked_or_masked | COVERED | 验证运行状态（被阻止或已脱敏），平台行为层面可观测 |

