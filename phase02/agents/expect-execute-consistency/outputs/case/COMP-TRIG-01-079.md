# COMP-TRIG-01-079

- **标题**: 触发事件 types 取值与过滤边界验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 pull_request types 取值边界（合法 open/merge 通过，非法拒绝）。

## 做了什么
Steps: case 语句判断 ACTION 是否命中 [open, merge] whitelist，输出 type_allowed / type_unexpected。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | step 含真实 case 判断，非必然 success |
| 2 | run_logs | positive | must_contain type_allowed | COVERED | case 语句真实判断 action ∈ {open, merge} |
| 3 | run_logs | negative | must_not_contain type_unexpected | COVERED | type=negative，case 语句 intentional 覆盖 |
| 4 | workflow_parse | negative | eval=llm_assisted | LLM_DEPENDENT | 非法 types 变体需人工验证 |
| 5 | run_created | negative | eval=llm_assisted | LLM_DEPENDENT | 默认 types 变体需人工验证 |
