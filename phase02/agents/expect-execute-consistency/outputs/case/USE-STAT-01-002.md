# USE-STAT-01-002
- **标题**: 使用 success() 带括号时报错应提示 GitCode 括号差异
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain success（报错应含状态函数名）；括号差异提示质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | success() 写法应导致校验失败 |
| 2 | error_message | positive | must_contain success | ✅ COVERED | 报错应含函数名（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 括号差异提示质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
