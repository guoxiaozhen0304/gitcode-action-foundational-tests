# COMPAT-PERM-01-004
- **标题**: permissions 命名差异——GitCode repository 权限项正常生效
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 GitCode 风格 `repository: read` 权限项被平台正确解析并正常生效。

## 做了什么
声明 `permissions: { repository: read }`，执行 checkout 后验证 README.md 可读。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals completed_success | COVERED | repository 权限生效时 checkout 和 cat 成功 |
| 2 | run_logs | positive | llm_assisted rubric "REPOSITORY_PERM_OK" | LLM_DEPENDENT | 需 LLM 辅助确认输出 |
| 3 | run_logs | negative | llm_assisted rubric "REPOSITORY_PERM_FAILED" | LLM_DEPENDENT | 需 LLM 辅助确认 |
| 4 | workflow_parse | negative | llm_assisted rubric | LLM_DEPENDENT | 需 LLM 判断 repository 权限项是否被解析接受 |
