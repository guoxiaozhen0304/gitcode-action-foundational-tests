# COMPAT-NEEDS-01-001
- **标题**: needs 上下文存在性与 outputs/result 字段对齐（规格矛盾仲裁）
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 needs 上下文中 outputs 取值正确性和 result 字段存在性，仲裁 context.md 规格矛盾。

## 做了什么
上游 job 声明 outputs.version，下游通过 needs 读取 outputs 和 result 并 echo 输出。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "NEEDS_VERSION=1.2.3" | COVERED | echo 含 `${{ needs.build.outputs.version }}` 输出，可验证 outputs 取值 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | NEEDS_RESULT 字段是否存在及取值需 LLM 辅助判断 |
| 3 | run_logs | negative | llm_assisted rubric | LLM_DEPENDENT | needs 在表达式中是否可用需 LLM 辅助判断 |
