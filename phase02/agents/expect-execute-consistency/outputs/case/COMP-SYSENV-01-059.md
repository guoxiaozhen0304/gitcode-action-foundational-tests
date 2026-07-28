# COMP-SYSENV-01-059

- **标题**: ATOMGIT 系统环境变量关键变量存在性
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 ATOMGIT_SHA、REF、REF_NAME、EVENT_NAME、WORKSPACE 等环境变量存在且非空。

## 做了什么
Step: 使用 `[ -n "$ATOMGIT_SHA" ] && echo yes || echo no` 等真实 shell 测试命令检查各变量。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain SHA_SET=yes | COVERED | `[ -n "$ATOMGIT_SHA" ]` 是真实验 shell 测试 |
| 2 | run_logs | positive | must_contain REF_SET=yes | COVERED | 同上 |
| 3 | run_logs | positive | must_contain EVENT_NAME_SET=yes | COVERED | 同上 |
| 4 | run_logs | positive | must_contain WORKSPACE_SET=yes | COVERED | 同上 |
| 5 | run_logs | positive | must_contain REPO_SET=yes | COVERED | 同上 |
| 6 | run_logs | positive | must_contain RUN_ID_SET=yes | COVERED | 同上 |
