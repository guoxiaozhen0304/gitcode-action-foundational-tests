# COMP-ARTIFACT-01-001
- **标题**: artifact 可在同 workflow 的 job 间正确传递
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
job1 上传 artifact，job2 通过 needs 依赖下载并验证内容一致性。

## 做了什么
1. build job: `mkdir -p dist && echo "hello artifact" > dist/app.txt` → `uses: upload-artifact`
2. verify job (needs: build): `uses: download-artifact` → `cat dist/app.txt`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 真实的 upload/download action 调用和文件操作，可能失败 |
| 2 | run_logs | positive | contains: hello artifact | COVERED | `cat dist/app.txt` 输出文件内容到日志 |
