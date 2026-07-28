# COMP-DIR-01-002
- **标题**: .github/workflows/ 下的 YAML 不被识别为 workflow
- **维度**: completeness
- **评级**: 完全不符

## 想测什么
.github/workflows/ci.yml 不被识别为 workflow，push 事件不会触发运行。

## 做了什么
workflow 内容为空（只有 `on:` 声明但无 jobs），trigger: push。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | equals: no_run_from_github_dir | UNVERIFIABLE | 目标不是 run_logs/run_status，且 workflow 体为空，没有 step 可产生可观测日志。需要外部平台 API 检查运行列表。 |
