# COMP-SUMMARY-01-002

- **标题**: summary 中不应暴露系统内部路径
- **维度**: 完备性
- **评级**: 完全不符

---

## 想测什么
验证 step summary 中不包含 Runner 内部绝对路径。

## 做了什么
Step: `echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"`（写入安全内容）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary | negative | must_not_contain /tmp/runner | VACUOUS | 步骤仅写入 "Results: OK"，从未输出 /tmp/runner；断言永远为真，安全行为未被触发（Rule 4） |
| 2 | step_summary | negative | must_not_contain /opt/actions | VACUOUS | 同上，步骤从未输出 /opt/actions |
