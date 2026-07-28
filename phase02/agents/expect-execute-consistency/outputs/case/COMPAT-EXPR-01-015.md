# COMPAT-EXPR-01-015
- **标题**: startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
实测 startsWith/endsWith 对混合大小写的求值行为，仲裁 GitHub 文档（不区分大小写）与 GitCode 文档（区分大小写）之间的矛盾。

## 做了什么
echo 输出 `${{ startsWith('Hello World', 'hello') }}` 和 `${{ endsWith('v1.0.rc', '.RC') }}` 的求值结果，再 echo "PROBE_DONE"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | 表达式求值不报错，status 检查可验证 |
| 2 | run_logs | positive | must_contain "PROBE_DONE" | COVERED | echo 输出可验证所有步骤完成 |
| 3 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | SW_RESULT/EW_RESULT 求值结果与文档一致性需 LLM 辅助判断 |
