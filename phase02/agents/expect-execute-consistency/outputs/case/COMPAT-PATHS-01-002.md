# COMPAT-PATHS-01-002
- **标题**: paths 过滤器 301 条越界测试
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 on.push.paths 配置 301 条（超过上限）时，平台应给出明确校验错误。

## 做了什么
配置 301 条 path 规则，step 中 echo "PATHS_301_OK"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | 301 条越界被拒绝时 run 不应成功 |
| 2 | error_message | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
