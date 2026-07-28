# USE-MASK-01-001  - **标题**: secret 脱敏文档描述与实际行为一致并给出缓解建议   - **维度**: usability/security   - **评级**: 断言一致

## 想测什么

日志中 secret 显示为 ***；文档若声明绕过风险，必须同时给出正确写法示例

## 做了什么

- 1. 在 workflow 中通过环境变量注入方式引用 secret（TEST_SECRET 已在仓库 secrets 中声明）
- 2. 一个步骤输出 secret 长度，另一个步骤直接输出 secret 值
- 3. 检查日志脱敏效果

- - [正向] 直接输出 secret 值时，日志中对应位置显示为 ***（原值绝不出现）
- - [非功能] 文档中的风险提示段落是否包含如何改的可操作建议

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=`***` | COVERED | run_logs+contains: $SECRET_VAL由secrets注入→平台脱敏输出***→GENUINE |
| 2 | run_logs | positive | must_not_contain_secret=`TEST_SECRET` | COVERED | must_not_contain_secret: 平台脱敏机制可验证→GENUINE |
| 3 | documentation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 文档缓解建议需LLM评估 |
