# USE-INPT-01-002
- **标题**: 使用 boolean 类型 input 时报错应提示仅支持 string
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain string（报错应说明仅支持 string 类型）；替代方案指引质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | boolean input 应触发校验失败 |
| 2 | error_message | positive | must_contain string | ✅ COVERED | 报错应含类型说明关键词 |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 替代方案指引质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
