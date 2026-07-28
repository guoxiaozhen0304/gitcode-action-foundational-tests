# COMP-CALL-01-003
- **标题**: 本地路径 workflow_call 完整 secrets 映射正常执行
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
本地路径（uses: ./.gitcode/workflows/reusable.yml）调用可复用 workflow，完整映射 secrets（OBS_AK/OBS_SK），验证正常执行。

## 做了什么
1. caller job：`uses: ./.gitcode/workflows/reusable.yml`，secrets 映射 OBS_AK 和 OBS_SK

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | job 级 `uses:` 真实调用，可能因 secret 映射问题失败 |
| 2 | run_logs | positive | must_contain: REUSABLE_OK | COVERED | 被调 workflow 步骤输出此标记 |
