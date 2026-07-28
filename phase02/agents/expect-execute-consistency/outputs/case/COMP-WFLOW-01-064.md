# COMP-WFLOW-01-064

- **标题**: workflow stages 阶段结构字段验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 stages map 格式通过校验，fail_fast true 时 build stage 某 job 失败中断后续 test stage。

## 做了什么
build stage 含 build 和 build-fail（exit 1）两个 job，test stage 含 test job；build stage fail_fast: true。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: failure | COVERED | build-fail 步骤 exit 1 导致失败 |
| 2 | run_logs | positive | must_contain: build_done | COVERED | build job echo "build_done" |
| 3 | run_logs | negative | must_not_contain: test_done | COVERED | fail_fast true 应阻止 test stage 执行 |
| 4 | workflow_parse | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定缺省 stages 字段等价于单 stage |
