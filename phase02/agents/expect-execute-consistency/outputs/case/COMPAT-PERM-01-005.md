# COMPAT-PERM-01-005
- **标题**: permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 `permissions: {}` 空对象时 ATOMGIT_TOKEN 的权限范围——读操作应成功，写操作应被拒绝。

## 做了什么
声明 `permissions: {}`，用 curl + ATOMGIT_TOKEN 分别尝试读操作（GET /user）和写操作（POST 创建 repo）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | llm_assisted rubric "读操作返回 200" | LLM_DEPENDENT | curl HTTP 状态码需 LLM 辅助判断 |
| 2 | run_logs | negative | llm_assisted rubric "写操作被拒绝" | LLM_DEPENDENT | 写操作返回 403/401 需 LLM 辅助判断 |
