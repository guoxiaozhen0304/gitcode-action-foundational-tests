# COMP-SUMMARY-01-002

- **标题**: summary 中不应暴露系统内部路径
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 step summary 中不包含 Runner 内部绝对路径。

## 做了什么
Step: `echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"`（写入安全内容）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary | negative | must_not_contain /tmp/runner | COVERED | Step 写入安全内容，harness 验证平台不注入内部路径到 summary；type=negative |
| 2 | step_summary | negative | must_not_contain /opt/actions | COVERED | 同上 |
