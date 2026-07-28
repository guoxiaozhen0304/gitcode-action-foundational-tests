# COMP-WFLOW-01-065
- **标题**: workflow post 后处理阶段字段验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
验证 post 阶段 run_always:true 时，主 job 失败后 post 仍执行。
## 做了什么
workflow_dispatch 触发，jobs: verify（成功）+ failing（exit 1）；post: run_always:true echo `post_done`。断言 run_status=failure, main_done 出现, post_done 出现。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: failure | GENUINE→COVERED | failing job exit 1，最终状态为失败 |
| 2 | run_logs | positive | must_contain: main_done | GENUINE→COVERED | verify job 正常 echo |
| 3 | run_logs | positive | must_contain: post_done | GENUINE→COVERED | post echo 应出现，验证 run_always 行为 |
