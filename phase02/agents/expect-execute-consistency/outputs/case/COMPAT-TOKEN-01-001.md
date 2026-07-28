# COMPAT-TOKEN-01-001
- **标题**: ATOMGIT_TOKEN 应正确返回有效令牌
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 ATOMGIT_TOKEN 在 GitCode 中正确返回有效令牌，能完成 API 认证且日志脱敏。
## 做了什么
通过 `${{ secrets.ATOMGIT_TOKEN }}` 引用令牌发起 API 调用，检查 HTTP 状态码和日志脱敏。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success | COVERED | 标准运行状态检查 |
| 2 | run_logs | positive | llm_assisted 判断api_status=200 | LLM_DEPENDENT | eval=llm_assisted，需人工确认状态码 |
| 3 | run_logs | negative | must_not_contain_secret=ATOMGIT_TOKEN | COVERED | 机密脱敏检查，Harness 可直接验证日志不含明文 |
