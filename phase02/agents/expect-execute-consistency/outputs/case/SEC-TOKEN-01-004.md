# SEC-TOKEN-01-004
- **标题**: 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原步骤仅 echo 字面量（断言 1 UNVERIFIABLE）。改为真实 API 调用：残留 token（fixture residual_token.txt）调 API，200 则 RESIDUAL_TOKEN_ACCEPTED_BAD + exit 1；当前 run token 调 API 验证 CURRENT_RUN_TOKEN_OPERATIONAL；断言全部确定化。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain CURRENT_RUN_TOKEN_OPERATIONAL | ✅ GENUINE | 真实 curl 200 后输出 |
| 2 | run_logs | negative | must_not_contain RESIDUAL_TOKEN_ACCEPTED_BAD | ✅ GENUINE | 残留 token 通过鉴权时输出并 exit 1 |
| 3 | api_response | negative | must_not_equal http_2xx_with_residual_token | ✅ COVERED | harness 外部复验 |
