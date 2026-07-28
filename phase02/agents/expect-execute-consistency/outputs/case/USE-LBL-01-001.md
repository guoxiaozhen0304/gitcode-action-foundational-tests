# USE-LBL-01-001
- **标题**: runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain nonexistent-os（报错应含用户指定标签原文）；可用标签列表提示质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 无匹配 runner 应失败 |
| 2 | error_message | positive | must_contain nonexistent-os | ✅ COVERED | 报错应含标签原文（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 可用标签列表提示质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
