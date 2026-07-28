# COMP-WFLOW-01-064
- **标题**: workflow stages 阶段结构字段验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
验证 stages map 格式，fail_fast true 时 build 失败中断后续 test stage，运行状态为 failure。
## 做了什么
workflow_dispatch 触发，build stage（fail_fast:true）含两个 job（成功+exit 1），test stage（fail_fast:false）含一个 job；期望 build_done 出现、test_done 不出现、状态为 failure。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: failure | GENUINE→COVERED | build-fail 有 exit 1，预期最终失败 |
| 2 | run_logs | positive | must_contain: build_done | GENUINE→COVERED | build 成功的 job echo 产生 |
| 3 | run_logs | negative | must_not_contain: test_done | GENUINE→COVERED | fail_fast 应在 test_done 标记出现前中断；若 test 未执行则不会被 echo |
| 4 | workflow_parse | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
