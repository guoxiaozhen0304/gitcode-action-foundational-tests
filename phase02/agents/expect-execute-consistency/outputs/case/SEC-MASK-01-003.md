# SEC-MASK-01-003
- **标题**: Secret 日志脱敏不可通过 base64 编码绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
加注释说明：base64 编码后的字符串值动态（取决于 secret 原值），schema 无"编码形式"确定性判定键，保留 llm_assisted；harness 可自行计算 base64(secret) 全文比对辅助。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret DEPLOY_TOKEN | ✅ GENUINE | 明文原值确定性检索（步骤真实 base64 编码并输出） |
| 2 | run_logs | negative | llm_assisted | 🔶 LLM_DEPENDENT | 编码形式遮蔽判定值动态 |

### 残留问题
base64 编码形式的判定依赖动态值，保留 llm_assisted（YAML 已注释，harness 可确定化辅助）。
