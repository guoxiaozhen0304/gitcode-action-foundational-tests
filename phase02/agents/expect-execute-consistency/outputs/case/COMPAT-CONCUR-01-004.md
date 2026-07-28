# COMPAT-CONCUR-01-004
- **标题**: concurrency preemption events 越界时行为差异   - **维度**: 兼容性   - **评级**: 部分不符
## 想测什么
验证 concurrency.preemption.events 为越界值（11）时被拒绝并给出有效范围提示。
## 做了什么
workflow_dispatch 触发，concurrency preemption.events 配置为 11（越界值），step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；系统应对越界值报错 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错应包含有效范围提示 |
说明：文本声明 events 为"11 个（越界值）"，但 YAML 中 preemption.events 值为数字 11 而非数组 [1,2,...11]，语义有偏差。文本称 GitHub 行为为拒绝，GitCode 可能不支持 events 字段，需 LLM 实际裁定。 |
