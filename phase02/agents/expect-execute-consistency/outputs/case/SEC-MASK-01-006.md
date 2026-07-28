# SEC-MASK-01-006
- **标题**: Secret 日志脱敏不可通过分片输出绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
同 SEC-MASK-01-004：加注释说明子串判定的动态性与 harness 辅助方式。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret DEPLOY_TOKEN | ✅ GENUINE | 明文原值确定性检索（步骤真实逐字符分片输出） |
| 2 | run_logs | negative | llm_assisted | 🔶 LLM_DEPENDENT | 分片后连续子串判定值动态 |

### 残留问题
保留 llm_assisted（YAML 已注释）。
