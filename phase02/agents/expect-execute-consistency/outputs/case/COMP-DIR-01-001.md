# COMP-DIR-01-001
- **标题**: .gitcode/workflows/ 下的 YAML 被正确识别并触发
- **维度**: completeness
- **评级**: 部分不符

## 想测什么
.gitcode/workflows/ 下的 YAML 被识别为 workflow，push 事件触发执行。

## 做了什么
1. step `Echo verify`：`echo "workflow recognized"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | push 触发真实 workflow 执行 |
| 2 | run_file_path | positive | equals: .gitcode/workflows/ci.yml | UNVERIFIABLE | 目标不是 run_logs/run_status，file_path 是平台元数据，需平台 API 返回 |
