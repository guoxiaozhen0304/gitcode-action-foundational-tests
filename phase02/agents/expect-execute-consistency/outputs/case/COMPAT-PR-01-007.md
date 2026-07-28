# COMPAT-PR-01-007
- **标题**: pull_request 不支持的 activity type（labeled）不应静默退化
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 GitCode 对 `pull_request.types: [labeled]`（非法type）的解析行为——解析阶段应明确报错而非静默退化。

## 做了什么
workflow 配置 `pull_request.types: [labeled]`，step输出 `echo "LABELED_TYPE_JOB_RAN"`；通过非labeled活动触发来探测types是否被静默忽略。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative | "若被静默接受则非labeled活动不应触发运行" | COVERED | run_list可观测；echo "LABELED_TYPE_JOB_RAN"若出现在列表中则证明types被忽略(R1 GENUINE) |
| 2 | save_result | positive | "解析/保存阶段应明确报错并列出合法types" | COVERED | save_result为平台解析日志(GENUINE R1)；对malformed config保存反馈可观测 |
