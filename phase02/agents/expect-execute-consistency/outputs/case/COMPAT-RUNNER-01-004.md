# COMPAT-RUNNER-01-004
- **标题**: 自定义特征标签不被支持时应给出可用标签列表
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: [gpu, nvidia]` 自定义标签不被支持时，报错应说明标签组合不可用并给出可用标签列表。

## 做了什么
workflow配置 `runs-on: [gpu, nvidia]`，step输出 `echo "hello"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | error_message | positive llm | "报错信息说明标签组合gpu,nvidia不可用" | COVERED | error_message为平台日志(GENUINE R1)；R5 LLM辅助判断报错内容是否说明不可用 |
| 2 | error_message | positive llm | "报错给出可用标签列表或标签格式指引" | COVERED | 同#1，平台报错信息可直接观测(GENUINE) |
