# USE-RUN-01-003
- **标题**: rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
验证重跑达到上限或超时后 UI 按钮应置灰且有 tooltip 明示原因，运行详情页显示已重跑次数。

## 做了什么
workflow 故意 exit 1 制造失败运行，用于后续重跑上限测试。断言依赖 LLM 判断 UI 可观测性。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | nonfunctional | 达到上限/超时后 UI 给出可理解提示 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
