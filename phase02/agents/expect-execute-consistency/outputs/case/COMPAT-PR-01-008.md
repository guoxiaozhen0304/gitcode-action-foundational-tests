# COMPAT-PR-01-008
- **标题**: pull_request 不支持的 activity type（ready_for_review）不应静默不触发
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 GitCode 对 `pull_request.types: [ready_for_review]`（非法type）的解析行为——不应静默接受后永不触发。

## 做了什么
workflow 配置 `pull_request.types: [ready_for_review]`，step输出 `echo "RFR_TYPE_JOB_RAN"`；draft→ready后观察是否触发。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_list | negative | "draft转正式后既不触发也无提示，记为缺陷" | COVERED | run_list可观测；echo "RFR_TYPE_JOB_RAN"若出现在列表中则证明types被忽略(GENUINE R1) |
| 2 | save_result | positive | "解析/保存阶段应明确报错并列出合法types" | COVERED | save_result为平台解析日志(GENUINE)，与007同策略 |
