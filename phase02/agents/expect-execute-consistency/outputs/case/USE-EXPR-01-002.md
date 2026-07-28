# USE-EXPR-01-002
- **标题**: 调用未知函数时报错应提示函数名错误与修正方向
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain unknownFunc（报错应含原始函数名）；修正方向提示质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 未知函数应导致校验失败 |
| 2 | error_message | positive | must_contain unknownFunc | ✅ COVERED | 报错应含函数名（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 修正方向提示质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
