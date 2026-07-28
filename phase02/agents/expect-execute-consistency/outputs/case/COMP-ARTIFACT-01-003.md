# COMP-ARTIFACT-01-003
- **标题**: artifact 保留期设置生效
- **维度**: completeness
- **评级**: 完全不符

## 想测什么
artifact 设置 retention-days: 1 后，保留期内可访问，超过保留期不可访问。

## 做了什么
1. upload job: `echo "temp" > temp.txt` → upload-artifact with retention-days: 1

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_available | positive | yes_within_retention | UNVERIFIABLE | 目标不是 run_logs/run_status，在 step 中无可观察产出的运行时检查，需要外部平台 API 探测 |
| 2 | artifact_available_after_expiry | negative | no_after_1_day | UNVERIFIABLE | 同上，需要等待一天后的平台 API 探测，step 内无产出 |
