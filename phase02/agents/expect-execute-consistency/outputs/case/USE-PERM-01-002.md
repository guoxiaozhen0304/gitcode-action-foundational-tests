# USE-PERM-01-002  - **标题**: 使用 GitHub 权限域命名时报错应给出 GitCode 对照表   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

YAML 校验报错，提示 GitCode 支持的权限域列表，并指出命名差异

## 做了什么

- 1. 在 workflow 中使用 permissions: contents: read

- - [负向] 不应静默忽略未知权限域
- - [非功能] 报错中应列出 GitCode 可用权限域列表

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: permissions:contents是GitHub命名→平台应拒绝 |
| 2 | error_message | positive | must_contain=`permissions` | COVERED | error_message+must_contain: 报错信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 对照表质量需LLM评估 |
