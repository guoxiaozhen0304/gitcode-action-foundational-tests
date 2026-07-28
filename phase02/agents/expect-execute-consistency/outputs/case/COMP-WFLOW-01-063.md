# COMP-WFLOW-01-063
- **标题**: workflow concurrency 并发控制字段验证   - **维度**: 完备性   - **评级**: 部分不符
## 想测什么
验证合法 concurrency 配置通过校验；max<1 被拒绝；preemption.events 含非 mr_id 被拒绝。
## 做了什么
workflow_dispatch 触发，concurrency 配置合法值（max:2, exceed-action:QUEUE, preemption.events:[mr_id]），echo `concurrency_ok`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | 合法配置正常执行 |
| 2 | run_logs | positive | must_contain: concurrency_ok | GENUINE→COVERED | 含 `${{ atomgit.run_id }}`，按 R6 GENUINE |
说明：文本要求负向验证 max<1 和 preemption.events 越界被拒绝，但 YAML 中无对应的负向步骤或负向断言。这两个验证点为 MISSING。 |
