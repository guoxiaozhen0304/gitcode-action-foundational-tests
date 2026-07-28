# USE-TYPE-01-002  - **标题**: 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

YAML 校验报错，列出 GitCode 支持的 types 取值，并给出 GitHub 对应关系

## 做了什么

- 1. 配置 on: pull_request: types: [opened, synchronize]

- - [负向] 不应静默通过校验并在运行时永远不被触发
- - [非功能] 报错中应列出 merge/open/reopen/update 并指出对应关系

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: types:[opened,synchronize]→GitHub命名→平台应拒绝或静默不触发 |
| 2 | error_message | positive | must_contain=`opened` | COVERED | error_message+must_contain: 错误信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: types对照表质量需LLM评估 |
