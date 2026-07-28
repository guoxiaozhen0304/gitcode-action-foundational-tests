# COMP-CTX-01-052

- **标题**: 上下文在条件表达式 if 中注入验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `if:` 条件中 `atomgit`、`env`、`needs.*.result` 上下文可正常解析，条件正确控制 step/job 执行。

## 做了什么
job 级 `if: ${{ atomgit.ref != '' }}`（true→执行），step 级 `if: ${{ atomgit.ref == 'refs/heads/does-not-exist' }}`（false→跳过不应输出 ref_match_unexpected），step 级 `if: ${{ env.ALWAYS_TRUE == 'yes' }}`（true→执行），下游 job 级 `if: ${{ needs.verify.result == 'success' }}`（true→执行）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: always | COVERED | 无条件 step 始终执行，echo 输出 |
| 2 | run_logs | positive | must_contain: conditional_env_passed | COVERED | env 条件为 true，步骤执行并 echo 输出 |
| 3 | run_logs | positive | must_contain: needs_result_passed | COVERED | needs.verify.result == 'success' 条件为 true，下游 job 执行并 echo 输出 |
| 4 | run_logs | negative | must_not_contain: ref_match_unexpected | COVERED | atomgit.ref 不等于 does-not-exist，条件为 false → 步骤不执行 → 该输出不应出现 |
