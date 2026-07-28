# USE-TYPE-01-002
- **标题**: 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain opened（报错应含非法 types 值）；对照关系提示质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 非法 types 值应校验失败 |
| 2 | error_message | positive | must_contain opened | ✅ COVERED | 报错应含非法值（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | types 对照提示质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
