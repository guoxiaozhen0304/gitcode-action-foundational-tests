# COMP-CALL-01-004

- **标题**: 未传 required secret 的 workflow_call 不应空值执行
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证调用方未传 required secret 时平台应在校验/调度期明确失败，不应以空值静默进入被调 workflow 执行。

## 做了什么
主 workflow 通过 job 级 `uses: ./.gitcode/workflows/reusable.yml` 调用，但不在 `secrets:` 下映射 required 的 `OBS_AK`/`OBS_SK`。被调 workflow 在执行时会输出 `UPLOAD_DONE`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | COVERED | 缺失 required secret 时平台应拒绝/失败，status != success 有意义 |
| 2 | run_logs | negative | must_contain: UPLOAD_DONE | COVERED | 若未传 secret 仍静默执行，被调 workflow 会输出 UPLOAD_DONE；断言其不出现 = 证实执行被阻止 |
| 3 | error_message | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
