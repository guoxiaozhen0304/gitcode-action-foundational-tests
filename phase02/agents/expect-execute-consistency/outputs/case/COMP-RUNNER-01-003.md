# COMP-RUNNER-01-003

- **标题**: 不存在的标签组合导致 job 排队或失败
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证不存在的 runs-on 标签导致 job 无法成功执行。

## 做了什么
runs-on: [nonexistent-os, x64, small]，step 仅 `echo "should not run"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | 不存在的 Runner 标签导致 job 排队/失败，platform 会自动拒绝，harness 观测 status != success |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工判断错误信息措辞 |
