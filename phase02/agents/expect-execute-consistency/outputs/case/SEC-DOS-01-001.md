# SEC-DOS-01-001
- **标题**: 大 artifact / 大 cache 必须受配额与边界限制
- **维度**: security
- **评级**: 断言一致

## 想测什么
超过大小上限的 artifact 上传不应成功写入，job 以 failure 结束。

## 做了什么
workflow dd 生成 1100MB 文件并 upload-artifact；断言 run_status 不为 success、job_status 为 failure。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal "success" | COVERED | 对应"超过大小上限的 artifact 上传绝不应成功写入"；platform 判定→GENUINE |
| 2 | job_status | positive | equals "failure" | COVERED | 对应"超限 job 的最终状态为 failure"；platform 判定→GENUINE |
