# COMPAT-TOKEN-01-001
- **标题**: ATOMGIT_TOKEN 应正确返回有效令牌
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ secrets.ATOMGIT_TOKEN }}` 返回有效令牌——API调用应返回200，且日志中令牌值被脱敏。

## 做了什么
step执行curl调API repo端点，使用 `$ATOMGIT_TOKEN` 和 `${{ atomgit.api_url }}` + `${{ atomgit.repository }}` 上下文，输出http状态码和done。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive llm | "api_status应为200，表明TOKEN有效" | COVERED | curl + $ATOMGIT_TOKEN为真实命令(GENUINE R1)；http状态码在日志中可观测 |
| 3 | run_logs | negative must_not_contain_secret | "日志中不应出现ATOMGIT_TOKEN明文" | COVERED | must_not_contain_secret校验(R4★平台脱敏机制) |
