# SEC-ORG-01-001
- **标题**: 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
visibility_change 抽象断言（equals 字面值）改为显式 llm_assisted + rubric（变更前后对照运行，LLM 辅助核验即时生效）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret ORG_SHARED_KEY | ✅ GENUINE | 步骤真实引用 secret，原值检索可判定 |
| 2 | run_logs | positive | equals empty_or_error_outside_scope | ✅ COVERED | 范围外输出可判定 |
| 3 | visibility_change | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 可见性变更即时生效需变更前后对照判读 |

### 残留问题
可见性变更的即时性判读保留 llm_assisted。
