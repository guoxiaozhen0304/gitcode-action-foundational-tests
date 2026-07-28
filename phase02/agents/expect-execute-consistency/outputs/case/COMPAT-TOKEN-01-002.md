# COMPAT-TOKEN-01-002
- **标题**: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ secrets.GITHUB_TOKEN }}` 在GitCode中应为空/未定义，API调用应返回401/403而非200，不应静默映射到ATOMGIT_TOKEN。

## 做了什么
step执行curl调API repo端点，使用 `${{ secrets.GITHUB_TOKEN }}` 作为token，输出http状态码。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative llm | "api_status应为401/403或空，不应为200" | COVERED | curl + ${{ secrets.GITHUB_TOKEN }}为GENUINE(R1上下文表达式)；http状态码可观测. 若GITHUB_TOKEN未定义，可能出现解析错误或空值导致curl失败 |
| 2 | error_message | nonfunctional llm | "报错应提示使用ATOMGIT_TOKEN替代" | COVERED | error_message为平台日志(GENUINE R1)；若静默为空且curl返回401则无报错，但这是可接受的负向结果 |
