# SEC-MASK-01-004
- **标题**: Secret 日志脱敏不可通过字符串拼接或插值绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
加注释说明：连续子串（超阈值）命中判定值动态，schema 无对应确定性键，保留 llm_assisted；harness 可截取 secret 子串自行比对。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret API_KEY | ✅ GENUINE | 明文原值确定性检索（步骤真实 cut 拼接输出） |
| 2 | run_logs | negative | llm_assisted | 🔶 LLM_DEPENDENT | 子串命中判定值动态 |

### 残留问题
子串判定依赖动态值与阈值，保留 llm_assisted（YAML 已注释）。
