# COMP-CTX-01-052
- **标题**: 上下文在条件表达式 if 中注入验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
if 条件中的上下文表达式被正确求值，atomgit.ref 条件匹配时步骤执行，env 条件匹配时步骤执行，needs.*.result 在 job 级 if 可解析。

## 做了什么
1. verify job（if: ${{ atomgit.ref != '' }}）：
   - step `Always run`：`echo "always"`
   - step `Negative ref match`（if: ${{ atomgit.ref == 'refs/heads/does-not-exist' }}）：`echo "ref_match_unexpected"` — 条件不成立应跳过
   - step `Conditional env`（if: ${{ env.ALWAYS_TRUE == 'yes' }}）：`echo "conditional_env_passed"`
2. downstream job（needs: verify, if: ${{ needs.verify.result == 'success' }}）：`echo "needs_result_passed"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: always | COVERED | echo 固定标记，无 if 阻挡 |
| 2 | run_logs | positive | must_contain: conditional_env_passed | COVERED | if 条件成立时执行 echo |
| 3 | run_logs | positive | must_contain: needs_result_passed | COVERED | needs.verify.result == 'success' 成立时执行 |
| 4 | run_logs | negative | must_not_contain: ref_match_unexpected | COVERED | if 条件不成立（ref 不是 does-not-exist），该步骤被跳过，不会输出 |
