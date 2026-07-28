# COMPAT-NEST-01-001
- **标题**: workflow_call 嵌套层数 - 2 层正常执行
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 2 层 workflow_call 嵌套（顶层调用第 2 层 reusable workflow）是否正常执行。

## 做了什么
顶层 workflow 使用 `uses: ./.gitcode/workflows/level2.yml` 调用 reusable workflow。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | 2 层嵌套正常执行应返回 success |
