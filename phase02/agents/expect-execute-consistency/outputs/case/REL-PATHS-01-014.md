# REL-PATHS-01-014
- **标题**: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
push变更300个文件(其中1个匹配paths规则)，workflow应被触发，不应因文件数=300异常。

## 做了什么
workflow on.push.paths:['src/**']，harness触发push含300个变更(含1个匹配)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed(success) | COVERED | 文本"workflow运行被创建"对应(harness通过run_status=success代为验证) |
