# USE-RUN-01-002
- **标题**: 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain runs-on（报错应含字段相关说明）；格式示例质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 单标签不匹配应失败 |
| 2 | error_message | positive | must_contain runs-on | ✅ COVERED | 报错应含字段名（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 格式指引质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
