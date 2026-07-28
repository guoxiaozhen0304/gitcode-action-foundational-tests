# USE-EXPR-01-001
- **标题**: 引用不存在的上下文属性时报错应包含原始表达式与错误类型
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
报错必含的原始属性名 nonexistent_property 为固定字符串，新增确定性断言 error_message must_contain；错误类型说明质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 引用不存在属性应导致失败 |
| 2 | error_message | positive | must_contain nonexistent_property | ✅ COVERED | 报错应含原始表达式（固定串可机器判定） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 错误类型说明质量判读 |

### 残留问题
报错文案质量判读保留 llm_assisted；关键内容已确定性覆盖。
