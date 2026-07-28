# COMP-WFLOW-01-061
- **标题**: workflow name 与 on 字段必填与类型验证   - **维度**: 完备性   - **评级**: 部分不符
## 想测什么
验证 name 可选、on 必填且为 map；on 为数组时平台拒绝。
## 做了什么
workflow_dispatch 触发，定义 name 和 on: workflow_dispatch，echo `RUN_ID=${{ atomgit.run_id }}` 和 `workflow_ok`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | 正常触发即成功 |
| 2 | run_logs | positive | must_contain: workflow_ok | GENUINE→COVERED | 含 `${{ atomgit.run_id }}`，按 R6 GENUINE |
说明：文本声称"on 为数组时平台拒绝"作为验证点，但 YAML 中无任何负向断言对应数组格式测试，也无可产生数组格式错误的步骤。该验证点在当前 YAML 中为 MISSING。 |
