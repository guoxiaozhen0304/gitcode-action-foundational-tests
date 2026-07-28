# USE-SECNAME-01-001
- **标题**: Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误
- **维度**: 易用性/安全性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain ATOMGIT_TOKEN（报错应含涉事 secret 名）；命名规则说明质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 保留前缀 secret 应报错 |
| 2 | error_message | positive | must_contain ATOMGIT_TOKEN | ✅ COVERED | 报错应含涉事名称（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 命名规则说明质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
