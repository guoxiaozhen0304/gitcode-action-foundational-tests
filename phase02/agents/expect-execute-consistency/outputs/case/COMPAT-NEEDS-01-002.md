# COMPAT-NEEDS-01-002
- **标题**: needs 上游 job 被跳过时的 result 取值语义
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 needs 上游 job 被 `if: false` 跳过时，`needs.<job>.result` 的取值语义。

## 做了什么
上游 job 用 `if: ${{ false }}` 恒跳过；下游用 `always()` 确保执行，echo 输出 `${{ needs.skipme.result }}`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "PROBE_DONE" | COVERED | echo 输出可验证下游 step 执行 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | SKIPPED_RESULT 取值需 LLM 辅助判断与 GitHub 语义一致性 |
